from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#   urlopen 으로 데이터 가져오기
res = req.urlopen(url)

#   BeautifulSoup 로 분석하기
soup = BeautifulSoup(res, "html.parser")

#   데이터 추출
title = soup.find("title").string
wf = soup.find("wf").string

print(title)
print(wf)