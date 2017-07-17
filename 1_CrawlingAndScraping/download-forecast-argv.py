import sys
import urllib.request as req
import urllib.parse as parse

# 입력값 체크
if len(sys.argv) <= 1 :
    print("USAGE : download-forecast-argv <Region Number>")
    sys.exit()

# 입력값을 변수에 저장
regionNumber = sys.argv[1]

api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# 매개변수 추가
values = { 'stnId' : regionNumber }
params = parse.urlencode(values)

# url 생성
url = api + "?" + params
print("url=", url)

# 다운로드
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)