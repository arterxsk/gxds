import requests as req, re, os, time
from bs4 import BeautifulSoup as par

data = {}
try:
    xkoki = open("cxkies/coki.text", "r").read()
    login = req.get("https://mbasic.facebook.com", cookies={"cookie": xkoki}).text
    if "mbasic_logout_button" in login:
        pass
    elif "Your Account is Locked" in login:
        os.system("rm -rf cxkies/coki.text")
        exit()
    else:
        os.system("rm -rf cxkies/coki.text")
        exit(" × INVALID COOKIES!")
except FileNotFoundError:
    os.system("clear")
    print(" ! YOU HAVEN'T LOGIN\n")
    cxkies = input(" > INPUT COOKIES: ")
    cokii = {"cookie": cxkies}
    login = req.get("https://mbasic.facebook.com", cookies=cokii).text
    if "mbasic_logout_button" in login:
        print(" √ LOGIN SUCCEED")
        time.sleep(3)
        os.system("mkdir cxkies")
        open("cxkies/coki.text", "a").write(cxkies)
    elif "Your Account is Locked" in login:
        exit(" × cxkies locked.")
    else:
        exit(" × Login failed, check your cookies again.")

os.system("clear")
print(" * Bot share facebook! Make sure the post is public.\n")
xlink = input(" > Link post: ")
xamt = int(input(" > Amount share: "))
print("")


class xshare:
    def __init__(self, coki):
        self.coki = coki

    def gasken(self, xamt, xlink):
        coki = {"cookie": self.coki}
        session = req.Session()
        soup = par(
            req.get(
                "https://mbasic.facebook.com/story.php?story_fbid=121925043701320&id=100076514745258&_rdr",
                cookies=coki,
            ).text,
            "html.parser",
        )
        link = soup.find("form", {"method": "post"}).get("action")
        dstg = ["fb_dtsg", "jazoest"]
        for x in soup.find_all("input"):
            if x.get("name") in dstg:
                data.update({x.get("name"): x.get("value")})
        data.update(
            {
                "comment_text": xlink,
            }
        )
        for x in range(xamt):
            kirim = session.post(
                "https://mbasic.facebook.com" + link, data=data, cookies=coki
            )
            x += 1
            if "YOU CANNOT COMMENT AT THIS TIME" in kirim.text:
                os.system("rm -rf cxkies/coki.text")
                exit(" × ACCOUNT IS LIMITED, PLEASE CHANGE COOKIES!")
            elif "Your Account is Locked" not in kirim.text:
                if x == 1:
                    print(f" \_> Share succeed {x} ")
                else:
                    print(f" |_> Share succeed {x} ")
            else:
                os.system("rm -rf cxkies/coki.text")
                exit("\n × Share failed.\n ! Login with new cookies\n")
        print("\n √ Program finished")


if __name__ == "__main__":
    xshare(open("cxkies/coki.text", "r").read()).gasken(xamt, xlink)
