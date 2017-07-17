from bs4 import BeautifulSoup
import urllib.request as req

#   월드 오브 워크래프트 위키
url = "https://ko.wikipedia.org/wiki/%EC%9B%94%EB%93%9C_%EC%98%A4%EB%B8%8C_%EC%9B%8C%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

#   확장팩 목록을 가져오려 함
#   확장팩 목록의 css 선택자 이외의 다른 부분에 대한 목록도 가져옴
list = soup.select("#mw-content-text > div > ul > li > a")

for a in list :
    name = a.get("title")
    if name :
        print("-", name )
