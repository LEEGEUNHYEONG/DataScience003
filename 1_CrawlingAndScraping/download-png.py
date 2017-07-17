import urllib.request

# 파일의 URL
url = "http://uta.pw/shodou/img/28/214.png"

# 파일 저장명
savename = "test.png"


# urlretrieve 이용한 다운로드
"""
urllib.request.urlretrieve(url, savename)
print("save complete !")
"""

# urlopen 이용한 다운로드
# 데이터를 파이썬 메모리에 올릴 수 있다는 차이점
mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("save complete!")

