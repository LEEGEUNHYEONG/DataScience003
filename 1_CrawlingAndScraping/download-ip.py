import urllib.request

# 읽어들일 데이터의 url
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
# 데이터를 읽음
data = res.read()

# 바이너리 데이터를 문자열로 변환
text = data.decode("utf-8")
print(text)