#   쿠키 사용을 위한 requests 설치
# pip3 install requests


import requests
from bs4 import BeautifulSoup

id = ""
pw = ""

session = requests.session()

login_info = {
    "m_id" : id,
    "m_passwd" : pw
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

level = soup.select_one("#container > div > div.sm_myinfo > div > p > span").get_text()
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()

print("level : " + level)
print("mileage cnt : " + mileage)
print("ecoin cnt : " + ecoin)


