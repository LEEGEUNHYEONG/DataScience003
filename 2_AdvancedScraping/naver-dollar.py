import datetime

from bs4 import BeautifulSoup
import urllib.request as req

#   HTML
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

#   HTML 분석
soup = BeautifulSoup(res, "html.parser")

#   데이터 추출
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string
print("usd/krw", price)

#   저장할 파일
t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") + ".txt"
with open(fname, "w", encoding="utf-8") as f:
    f.write(price)


