import urllib.request
import urllib.parse

api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# 매개변수 추가
values = { 'stnId' : '108' }
params = urllib.parse.urlencode(values)

# url 생성
url = api + "?" + params
print("url=", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)