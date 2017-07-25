import matplotlib.pyplot as plt
import pandas as pd
import json

#   출현 빈도 데이터 읽기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

#   언어마다 계산
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]) :
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic) :
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate (fq) :
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v ) / 2

#   Pandas 의 Dataframe 에 입력
asclist = [[chr(n) for n in range(97, 97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)

#   그래프
plt.style.use('ggplot')
#df.plot(kind="bar", subplots=True, ylim=(0, 0.15))
df.plot(kind="line", subplots=True, ylim=(0, 0.15))
#plt.savefig("lang-plot.png")
plt.show()
