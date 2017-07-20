#   Beautifualsoup4 사용을 위한 설치
# pip3 install beautifulsoup4

from bs4 import BeautifulSoup


# 분석하고자 하는 HTML
html = """
<html>
    <title>
        Title 테스트
    </title>
    <body>
        <h1>스크레이핑이란?</h1>
        <p>웹페이지를 분석하는 것 </p>
        <p>원하는 부분을 추출하는 것 </p>
    </body>
</html>
"""

# HTML 분석하기
#soup = BeautifulSoup(html, 'html.parser')

#원하는 부분 추출
"""
h1 = soup.body.h1
p1 = soup.body.p
p2 = p1.next_sibling.next_sibling

# 요소의 글자 출력
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
"""

# find 로 원하는 부분 추출
"""
title = soup.find(id="title")
body = soup.find(id="body")

#   Error 발생
print("#title="+title.string)
print("#body="+body.string)
"""

html2 = """
<html><body>
        <ul>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
        </ul>
</body></html>
"""

soup2 = BeautifulSoup(html2, 'html.parser')

#   find_all 로 추출하기
links = soup2.find_all("a")

#   링크 목록 출력
for a in links :
    href = a.attrs['href']
    text = a.string
    print(text, " > ", href)
