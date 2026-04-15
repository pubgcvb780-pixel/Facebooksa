import os
import sys
import time
import uuid
import requests
import json
import re
import warnings
import subprocess

# تجاهل التحذيرات
os.environ['PYTHONWARNINGS'] = 'ignore'
warnings.filterwarnings("ignore")

# ================== إعداد اللوق ==================
def log_info(msg):
    print(f"[INFO] {msg}")

def log_error(msg):
    print(f"[ERROR] {msg}")

# ================== تثبيت المكتبات المفقودة ==================
def install_package(package, pip_name=None):
    if pip_name is None:
        pip_name = package
    try:
        __import__(package)
        print(f"✅ {package} موجود بالفعل")
        return True
    except ImportError:
        print(f"📦 جاري تثبيت {pip_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name, "--quiet"])
            print(f"✅ تم تثبيت {package}")
            return True
        except Exception as e:
            print(f"⚠️ فشل تثبيت {package}: {e}")
            return False

print("جاري التحقق من المكتبات...")


try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "packaging", "--upgrade", "--quiet"])
    print("✅ تم تحديث packaging")
except:
    pass

installed = {}
libraries = [
    ("PIL", "Pillow"),
    ("telebot", "pyTelegramBotAPI"),
    ("pydub", "pydub"),
    ("user_agent", "user_agent")
]

for lib, pip_name in libraries:
    installed[lib] = install_package(lib, pip_name)

print("=" * 50)

# استيراد المكتبات
PIL_AVAILABLE = False
PYDUB_AVAILABLE = False
TELEBOT_AVAILABLE = False
USER_AGENT_AVAILABLE = False

if installed.get("PIL", False):
    try:
        from PIL import Image
        PIL_AVAILABLE = True
    except ImportError:
        pass

if installed.get("pydub", False):
    try:
        from pydub import AudioSegment
        PYDUB_AVAILABLE = True
    except ImportError:
        pass

if installed.get("telebot", False):
    try:
        import telebot
        TELEBOT_AVAILABLE = True
    except ImportError:
        pass

if installed.get("user_agent", False):
    try:
        from user_agent import generate_user_agent
        USER_AGENT_AVAILABLE = True
    except ImportError:
        pass

def generate_user_agent_simple():
    return "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"

# ================== إنشاء المجلدات ==================
for folder in ["images", "results", "user_audio_files"]:
    try:
        os.makedirs(folder, exist_ok=True)
    except:
        pass

# ================== ملفات البيانات ==================
user_voices_file = "user_voices.json"
auth_session_file = "sessions.json"
stats_file_path = "bot_stats.json"
settings_file_path = "bot_settings.json"

# ================== إعدادات الـ API ==================
base_url = "https://voiceslab.io"
temp_api_url = "https://api.internal.temp-mail.io/api/v3"
CORRECTION_API_URL = "https://api-inference.huggingface.co/models/mohamed-khaled/arabic-text-correct"
CORRECTION_API_KEY = ""

# ================== دوال تحسين الصور ==================
class ImageOptimizer:
    @staticmethod
    def optimize_image(input_path, output_path, quality=90):
        if not PIL_AVAILABLE:
            try:
                with open(input_path, 'rb') as f_in:
                    with open(output_path, 'wb') as f_out:
                        f_out.write(f_in.read())
                return True
            except:
                return False
        
        try:
            img = Image.open(input_path)
            if img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                if img.mode == 'RGBA':
                    rgb_img.paste(img, mask=img.split()[3])
                else:
                    rgb_img.paste(img)
                img = rgb_img
            
            max_size = 2000
            if img.size[0] > max_size or img.size[1] > max_size:
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            return True
        except Exception as e:
            print(f"خطأ في تحسين الصورة: {e}")
            try:
                with open(input_path, 'rb') as f_in:
                    with open(output_path, 'wb') as f_out:
                        f_out.write(f_in.read())
                return True
            except:
                return False

# ================== دوال معالجة الصور ==================
class ImageProcessor:
    URL = "https://pornworks.com/api/v2"

    def upload(self, path):
        try:
            with open(path, 'rb') as f:
                files = {'file': (os.path.basename(path), f, 'image/jpeg')}
                headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
                r = requests.put(f"{self.URL}/uploads/undress", headers=headers, files=files, timeout=60)

            if r.status_code == 400:
                if "child" in r.text.lower() or "adolescent" in r.text.lower():
                    return "CHILD_DETECTED"
                return None
            
            if r.status_code in [200, 201, 202]:
                data = r.json()
                return data.get("url") or data.get("data", {}).get("url")
        except Exception as e:
            print(f"خطأ في الرفع: {e}")
        return None

    def generate(self, url):
        try:
            r = requests.post(f"{self.URL}/generate/undress", headers={
                'User-Agent': 'Mozilla/5.0',
                'Content-Type': 'application/json'
            }, json={"image": url, "gender": "auto"}, timeout=60)
            
            if r.status_code in [200, 201, 202]:
                data = r.json()
                return data.get("id") or data.get("data", {}).get("id")
        except Exception as e:
            print(f"خطأ في التوليد: {e}")
        return None

    def wait_done(self, gen_id):
        for _ in range(60):
            try:
                r = requests.get(f"{self.URL}/generations/{gen_id}/state", headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
                if r.status_code == 200:
                    data = r.json()
                    state = data.get("state") or data.get("data", {}).get("state", "")
                    if state in ["done", "completed", "success", "finished", "succeeded"]:
                        return True
                time.sleep(2)
            except Exception as e:
                print(f"خطأ في التحقق: {e}")
                time.sleep(2)
        return False

    def result(self, gen_id):
        try:
            r = requests.get(f"{self.URL}/generations/{gen_id}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=60)
            if r.status_code == 200:
                data = r.json()
                results = data.get("results") or data.get("data", {}).get("results", {})
                image_url = results.get("image") or results.get("output") or results.get("url") or results.get("result")
                if image_url:
                    if not image_url.startswith("http"):
                        if image_url.startswith("//"):
                            image_url = f"https:{image_url}"
                        elif image_url.startswith("/"):
                            image_url = f"https://pornworks.com{image_url}"
                    return image_url
        except Exception as e:
            print(f"خطأ في جلب النتيجة: {e}")
        return None

# ================== دوال استنساخ الصوت ==================
def load_settings():
    default_settings = {"status": "free", "paid_users": {}, "correction_enabled": True}
    if not os.path.exists(settings_file_path):
        return default_settings
    try:
        with open(settings_file_path, "r") as f:
            data = json.load(f)
            if "correction_enabled" not in data:
                data["correction_enabled"] = True
            return data
    except:
        return default_settings

def save_settings(settings_data):
    with open(settings_file_path, "w") as f:
        json.dump(settings_data, f, indent=2)

def correct_text_with_ai(text):
    settings = load_settings()
    if not settings.get("correction_enabled", True):
        return text
    if not CORRECTION_API_KEY:
        return text
    
    try:
        headers = {"Authorization": f"Bearer {CORRECTION_API_KEY}"}
        payload = {"inputs": text}
        response = requests.post(CORRECTION_API_URL, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', text)
        return text
    except:
        return text

def load_user_voices():
    if not os.path.exists(user_voices_file): return {}
    try:
        with open(user_voices_file, "r") as f:
            data = json.load(f)
            for uid in data:
                if not isinstance(data[uid], list):
                    data[uid] = []
            return data
    except: 
        return {}

def save_user_voices(data):
    with open(user_voices_file, "w") as f:
        json.dump(data, f, indent=2)

def add_user_voice(user_id, voice_name, voice_id, session_cookies, local_file_path=None, file_id=None):
    voices_db = load_user_voices()
    uid = str(user_id)
    if uid not in voices_db:
        voices_db[uid] = []
    elif not isinstance(voices_db[uid], list):
        voices_db[uid] = []
    
    voices_db[uid].append({
        "name": voice_name,
        "voiceId": voice_id,
        "session": session_cookies,
        "file_id": file_id,
        "local_file": local_file_path,
        "created": time.time()
    })
    save_user_voices(voices_db)
    return voice_name

def get_user_voices(user_id):
    data = load_user_voices()
    uid = str(user_id)
    if uid not in data:
        return []
    if not isinstance(data[uid], list):
        return []
    return data[uid]

def create_new_temp_email():
    try:
        r = requests.post(f"{temp_api_url}/email/new", json={"min_name_length": 10, "max_name_length": 10}, timeout=15)
        return r.json().get("email")
    except:
        return f"{uuid.uuid4().hex[:10]}@temp-mail.org"

def fetch_csrf_token():
    try:
        r = requests.get(f"{base_url}/api/auth/csrf", timeout=15)
        return r.json().get("csrfToken")
    except:
        return ""

def start_email_signin(email, csrf):
    data = {"email": email, "callbackUrl": f"{base_url}/en/dashboard/voice-cloning", "redirect": "false", "csrfToken": csrf, "json": "true"}
    return requests.post(f"{base_url}/api/auth/signin/email", data=data, timeout=15)

def poll_for_callback(email):
    for _ in range(30):
        try:
            r = requests.get(f"{temp_api_url}/email/{email}/messages", timeout=10)
            if r.ok and r.json():
                m = r.json()[0]
                link = re.search(r"https?://[^\s'\"<>]+", m.get("body_text", "") + m.get("body_html", ""))
                if link:
                    return link.group(0).replace("&amp;", "&")
        except:
            pass
        time.sleep(3)
    raise TimeoutError("Timeout waiting for email link")

def follow_and_check(link):
    session = requests.Session()
    r = session.get(link, allow_redirects=True, timeout=15)
    cookies = {k: v for k, v in session.cookies.items() if "next-auth" in k.lower() or "session" in k.lower()}
    return r, cookies

def is_session_valid(cookies):
    if not cookies:
        return False
    header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    try:
        r = requests.post(f"{base_url}/api/get-user-info", headers={'Cookie': header}, timeout=10)
        data = r.json().get("data", {})
        left = data.get("clone_credits", {}).get("left_credits", 0)
        return left > 5
    except:
        return False

def ensure_authenticated_session(force_new=False):
    if not force_new:
        if os.path.exists(auth_session_file):
            with open(auth_session_file, "r") as f:
                saved = json.load(f)
                if is_session_valid(saved.get("cookies")):
                    return saved

    email = create_new_temp_email()
    csrf = fetch_csrf_token()
    start_email_signin(email, csrf)
    link = poll_for_callback(email)
    _, cookies = follow_and_check(link)
    res = {"email": email, "cookies": cookies}
    with open(auth_session_file, "w") as f:
        json.dump(res, f)
    return res

def upload_voice_file(audio_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            if not os.path.exists(audio_path):
                return False, None, None

            sess = ensure_authenticated_session(force_new=(attempt > 0))
            cookies = sess["cookies"]
            if not cookies:
                raise Exception("No cookies")

            header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
            url = f"{base_url}/api/create-voice"

            with open(audio_path, "rb") as f:
                files = [("audio", ("audio.mp3", f, "audio/mpeg"))]
                data = {"title": "voice", "language": "ar"}
                r = requests.post(url, data=data, files=files, headers={'Cookie': header}, timeout=60)

            if r.status_code != 200:
                raise Exception(f"HTTP {r.status_code}")

            result = r.json()
            vid = result.get("voiceId")
            if vid:
                return True, vid, cookies
            else:
                raise Exception("No voiceId")

        except Exception as e:
            print(f"محاولة {attempt+1} فشلت: {e}")
            if attempt == max_retries - 1:
                return False, None, None
            time.sleep(2)
    return False, None, None

def synthesize_text_to_audio(text, voice_id, cookies):
    header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    payload = {
        "text": text, 
        "voiceId": voice_id, 
        "isPublicVoice": False, 
        "settings": {"rate": 0, "volume": 0, "pitch": 0}
    }
    try:
        r = requests.post(f"{base_url}/api/clone-voice", json=payload, headers={'Cookie': header, 'Content-Type': 'application/json'}, timeout=60)
        res = r.json()
        if "Character limit exceeded" in str(res):
            return "LIMIT", cookies
        return res.get("audioUrl"), cookies
    except Exception:
        return None, cookies

def synthesize_long_text(text, voice_id, cookies):
    parts = [text[i:i+150] for i in range(0, len(text), 150)]
    results = []
    curr_cookies = cookies
    for p in parts:
        url, curr_cookies = synthesize_text_to_audio(p, voice_id, curr_cookies)
        if url == "LIMIT":
            new_sess = ensure_authenticated_session(force_new=True)
            curr_cookies = new_sess["cookies"]
            url, curr_cookies = synthesize_text_to_audio(p, voice_id, curr_cookies)
        if url and url != "LIMIT":
            results.append(url)
        time.sleep(1)
    return results, curr_cookies

def merge_audio_files(urls, out):
    if not PYDUB_AVAILABLE:
        return None
    try:
        combined = AudioSegment.empty()
        for i, u in enumerate(urls):
            r = requests.get(u, timeout=30)
            tmp = f"tmp_{i}.mp3"
            with open(tmp, "wb") as f:
                f.write(r.content)
            combined += AudioSegment.from_mp3(tmp)
            os.remove(tmp)
        combined.export(out, format="mp3")
        return out
    except Exception as e:
        print(f"خطأ في دمج الصوت: {e}")
        return None

# ================== بوت التيليجرام ==================
if TELEBOT_AVAILABLE:
    # لن نقوم بإنشاء البوت الآن، سننشئه بعد إدخال التوكن
    voice_user_state = {}

    def voice_main_markup():
        m = telebot.types.InlineKeyboardMarkup(row_width=2)
        btn1 = telebot.types.InlineKeyboardButton("🎤 استنساخ سريع", callback_data="quick")
        btn2 = telebot.types.InlineKeyboardButton("➕ إضافة صوت", callback_data="add")
        btn3 = telebot.types.InlineKeyboardButton("📁 أصواتك", callback_data="list")
        btn4 = telebot.types.InlineKeyboardButton("👤 المطور", url="https://t.me/p7s7s")
        btn5 = telebot.types.InlineKeyboardButton("📷 معالجة صور", callback_data="image_help")
        btn6 = telebot.types.InlineKeyboardButton("📢 القناة", url="https://t.me/ZVBZBZB2")
        m.add(btn1, btn2)
        m.add(btn3, btn4)
        m.add(btn5, btn6)
        return m

    def setup_handlers(bot):
        """تعيين معالجات البوت"""
        
        @bot.callback_query_handler(func=lambda c: c.data == "image_help")
        def image_help(c):
            bot.answer_callback_query(c.id)
            bot.send_message(c.message.chat.id, 
                "📷 **معالجة الصور**\n\n"
                "للاستخدام: أرسل الصورة مباشرة\n"
                "سأقوم بمعالجتها وإرسال النتيجة\n\n"
                "⚠️ للبالغين فقط",
                parse_mode='Markdown')

        @bot.callback_query_handler(func=lambda c: c.data == "toggle_correction")
        def toggle_correction(c):
            settings = load_settings()
            settings["correction_enabled"] = not settings.get("correction_enabled", True)
            save_settings(settings)
            new_status = "مفعل ✅" if settings["correction_enabled"] else "معطل ❌"
            bot.answer_callback_query(c.id, f"تم {new_status} تصحيح النص")

        @bot.callback_query_handler(func=lambda c: True)
        def voice_calls(c):
            uid = c.from_user.id
            if c.data == "quick":
                voice_user_state[uid] = {"s": "wait_audio_q"}
                bot.send_message(c.message.chat.id, "🎤 أرسل البصمة الآن:")
            elif c.data == "add":
                voice_user_state[uid] = {"s": "wait_audio_s"}
                bot.send_message(c.message.chat.id, "➕ أرسل البصمة لحفظها:")
            elif c.data == "list":
                vs = get_user_voices(uid)
                if not vs:
                    return bot.answer_callback_query(c.id, "📭 لا توجد أصوات")
                m = telebot.types.InlineKeyboardMarkup()
                for i, v in enumerate(vs):
                    m.add(telebot.types.InlineKeyboardButton(v['name'], callback_data=f"v_{i}"))
                bot.edit_message_text("📁 اختر صوتاً:", c.message.chat.id, c.message.message_id, reply_markup=m)
            elif c.data.startswith("v_"):
                idx = int(c.data.split("_")[1])
                vs = get_user_voices(uid)
                if idx >= len(vs):
                    return bot.answer_callback_query(c.id, "❌ الصوت غير موجود")
                voice_user_state[uid] = {"s": "wait_text", "voice": vs[idx]}
                bot.send_message(c.message.chat.id, f"📝 أرسل النص لاستنساخه بصوت: {vs[idx]['name']}")

        @bot.message_handler(content_types=['voice', 'audio'])
        def voice_handle_audio(m):
            uid = m.from_user.id
            if uid not in voice_user_state:
                bot.reply_to(m, "❌ أرسل /start أولاً")
                return
            
            media = m.voice if m.voice else m.audio
            file_info = bot.get_file(media.file_id)
            
            filename = f"{uid}_{int(time.time())}_{media.file_id}.mp3"
            file_path = os.path.join("user_audio_files", filename)
            
            with open(file_path, "wb") as f:
                f.write(bot.download_file(file_info.file_path))
            
            if voice_user_state[uid]["s"] == "wait_audio_q":
                voice_user_state[uid] = {"s": "wait_text_q", "path": file_path}
                bot.reply_to(m, "✅ تم! الآن أرسل النص:")
            elif voice_user_state[uid]["s"] == "wait_audio_s":
                voice_user_state[uid] = {"s": "wait_name", "path": file_path, "fid": media.file_id}
                bot.reply_to(m, "📝 أرسل اسماً لهذا الصوت:")

        @bot.message_handler(content_types=['photo', 'document'])
        def voice_handle_image(m):
            msg = bot.reply_to(m, "📷 جاري معالجة الصورة...")
            
            try:
                if m.photo:
                    file_id = m.photo[-1].file_id
                else:
                    if not m.document.mime_type.startswith('image/'):
                        bot.edit_message_text("❌ هذا الملف ليس صورة", m.chat.id, msg.message_id)
                        return
                    file_id = m.document.file_id
                
                file_info = bot.get_file(file_id)
                uid = str(uuid.uuid4())[:8]
                image_path = f"images/{uid}.jpg"
                
                bot.edit_message_text("📥 جاري تحميل الصورة...", m.chat.id, msg.message_id)
                
                with open(image_path, "wb") as f:
                    f.write(bot.download_file(file_info.file_path))
                
                bot.edit_message_text("📤 جاري الرفع للمعالجة...", m.chat.id, msg.message_id)
                
                processor = ImageProcessor()
                upload_result = processor.upload(image_path)
                
                if upload_result == "CHILD_DETECTED":
                    bot.edit_message_text("❌ تم رفض الصورة - يمنع معالجة صور القُصَّر", m.chat.id, msg.message_id)
                    return
                
                if not upload_result:
                    bot.edit_message_text("❌ فشل رفع الصورة", m.chat.id, msg.message_id)
                    return
                
                bot.edit_message_text("⚙️ جاري المعالجة... (قد يستغرق دقيقة)", m.chat.id, msg.message_id)
                
                gen_id = processor.generate(upload_result)
                if not gen_id:
                    bot.edit_message_text("❌ فشل بدء المعالجة", m.chat.id, msg.message_id)
                    return
                
                if not processor.wait_done(gen_id):
                    bot.edit_message_text("❌ انتهت المهلة، حاول مرة أخرى", m.chat.id, msg.message_id)
                    return
                
                bot.edit_message_text("📥 جاري تحميل النتيجة...", m.chat.id, msg.message_id)
                
                result_url = processor.result(gen_id)
                if not result_url:
                    bot.edit_message_text("❌ فشل جلب النتيجة", m.chat.id, msg.message_id)
                    return
                
                result_response = requests.get(result_url, timeout=60)
                temp_path = f"results/temp_{uid}.jpg"
                final_path = f"results/final_{uid}.jpg"
                
                with open(temp_path, "wb") as f:
                    f.write(result_response.content)
                
                optimizer = ImageOptimizer()
                optimizer.optimize_image(temp_path, final_path)
                
                with open(final_path, "rb") as f:
                    bot.send_document(m.chat.id, f, caption="✅ تمت المعالجة بنجاح!")
                
                bot.delete_message(m.chat.id, msg.message_id)
                
                for path in [image_path, temp_path, final_path]:
                    try:
                        if os.path.exists(path):
                            os.remove(path)
                    except:
                        pass
                        
            except Exception as e:
                bot.edit_message_text(f"❌ حدث خطأ: {str(e)[:100]}", m.chat.id, msg.message_id)

        @bot.message_handler(func=lambda m: True)
        def voice_handle_text(m):
            uid = m.from_user.id
            
            if m.text == '/start':
                bot.send_message(m.chat.id, 
                    "🎤 **البوت المتكامل**\n\n"
                    "الخدمات المتوفرة:\n"
                    "• 🎤 استنساخ الصوت\n"
                    "• 📷 معالجة الصور\n\n"
                    "📌 **للاستخدام:**\n"
                    "- أرسل صورة لمعالجتها\n"
                    "- اختر من الأزرار لاستنساخ الصوت\n\n"
                    "👨‍💻 المطور: @p7s7s",
                    reply_markup=voice_main_markup(),
                    parse_mode='Markdown')
                return
            
            if uid not in voice_user_state:
                bot.reply_to(m, "❌ أرسل /start أولاً")
                return
            
            state = voice_user_state[uid]
            
            if state["s"] == "wait_name":
                msg = bot.reply_to(m, "⏳ جاري الحفظ...")
                success, vid, sess = upload_voice_file(state["path"])
                if success:
                    add_user_voice(uid, m.text, vid, sess, state["path"], state.get("fid"))
                    bot.edit_message_text("✅ تم الحفظ بنجاح!", m.chat.id, msg.message_id)
                else:
                    bot.edit_message_text("❌ فشل الرفع.", m.chat.id, msg.message_id)
                voice_user_state.pop(uid)
                
            elif state["s"] in ["wait_text_q", "wait_text"]:
                original_text = m.text
                corrected = correct_text_with_ai(original_text)
                if corrected != original_text:
                    bot.send_message(m.chat.id, f"📝 تم تصحيح النص:\n{corrected}")
                text_to_use = corrected
                
                msg = bot.reply_to(m, "🎤 جاري المعالجة... قد يستغرق دقيقة")
                
                if state["s"] == "wait_text_q":
                    success, vid, sess = upload_voice_file(state["path"])
                    if not success:
                        bot.edit_message_text("❌ فشل رفع الصوت.", m.chat.id, msg.message_id)
                        voice_user_state.pop(uid)
                        return
                    if os.path.exists(state["path"]):
                        os.remove(state["path"])
                else:
                    vid, sess = state["voice"]["voiceId"], state["voice"]["session"]
                
                urls, _ = synthesize_long_text(text_to_use, vid, sess)
                
                if not urls:
                    bot.edit_message_text("❌ فشل الاستنساخ.", m.chat.id, msg.message_id)
                    voice_user_state.pop(uid)
                    return
                
                out = f"res_{uid}.mp3"
                merged = merge_audio_files(urls, out)
                
                if merged and os.path.exists(merged):
                    with open(merged, "rb") as f:
                        bot.send_audio(m.chat.id, f, caption="✅ تم الاستنساخ بنجاح!", title="PS @p7s7s", performer="PS @p7s7s")
                    os.remove(merged)
                else:
                    for u in urls:
                        try:
                            bot.send_audio(m.chat.id, u)
                        except:
                            pass
                
                try:
                    bot.delete_message(m.chat.id, msg.message_id)
                except:
                    pass
                voice_user_state.pop(uid)

    # ================== التشغيل ==================
    def main():
        print("\n" + "=" * 50)
        BOT_TOKEN = input("📝 أدخل توكن البوت: ").strip()
        print("=" * 50)
        
        if not BOT_TOKEN:
            print("❌ لا يمكن تشغيل البوت بدون توكن!")
            return
        
        if ":" not in BOT_TOKEN:
            print("❌ توكن البوت غير صالح! يجب أن يحتوي على نقطتين (:)")
            print("مثال: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
            return
        
        # إنشاء البوت بالتوكن
        bot = telebot.TeleBot(BOT_TOKEN)
        
        # تعيين المعالجات
        setup_handlers(bot)
        
        
        print("✅ البوت يعمل بنجاح!")
        print(f"📱 توكن البوت: {BOT_TOKEN[:15]}...")
        print(f"📦 Pillow (تحسين الصور): {'✅' if PIL_AVAILABLE else '❌'}")
        print(f"📦 Pydub (دمج الصوت): {'✅' if PYDUB_AVAILABLE else '❌'}")
       
        print("الخدمات المتوفرة:")
        print("  • 🎤 استنساخ الصوت - أرسل /start")
        print("  • 📷 معالجة الصور - أرسل صورة")
       
        print("اضغط Ctrl+C للإيقاف")
        
        
        try:
            bot.infinity_polling(timeout=30, long_polling_timeout=30)
        except KeyboardInterrupt:
            print("\n👋 تم إيقاف البوت")
        except Exception as e:
            print(f"❌ خطأ: {e}")

    if __name__ == "__main__":
        main()

else:
    print("❌ لم يتم تثبيت pyTelegramBotAPI!")
    print("\nيرجى التثبيت يدوياً باستخدام الأمر:")
    print("pip install pyTelegramBotAPI")
