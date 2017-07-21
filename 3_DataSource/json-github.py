import urllib.request as req
import os.path
import json

#   json 다운로드
url = "https://api.github.com/repositories"

#   파일로 저장
savename = "ropo.json"
if not os.path.exists(savename) :
    req.urlretrieve(url, savename)

#   json 분석
items = json.load(open(savename, "r", encoding="utf-8"))

"""
s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)
"""


#   출력
for item in items :
    print(item["name"] + " - " + item["owner"]["login"])


"""
#   출력
s = json.dumps(items)
print(s)
"""