#!/usr/bin/env python3
import cgi, os.path
from sklearn.externals import joblib

pklfile = os.path.dirname(__file__) + "/freq.pkl"
clf = joblib.load(pklfile)

#   텍스트 입력 양식 출력
def show_form(text, msg="") :
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
        <html><body><form>
        <textarea name = "text" rows = "8" cols = "40">{0}</textarea>
        <p><input type = "submit" value = "submit"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(cgi.escape(text), msg))

#   판정하기
def detect_lang(text) :
    #   출현 빈도 구하기
    text = text.lower()
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]
    for ch in text :
        n = ord(ch) - code_a
        if 0 <= n < 26 : cnt[n] += 1
    total = sum(cnt)
    if total == 0: return "입력이 없습니다. "
    freq = list(map(lambda n : n/total, cnt))

    #   예측하기
    res = clf.predict([freq])

    #   한국어로 변환
    lang_dic = {"en":"en", "fr":"Fr", "id":"id", "tl":"tl"}
    return lang_dic[res[0]]

#   form 값 읽기
form = cgi.FieldStorage()
text = form.getvalue("text", default="")
msg = ""

if text != "" :
    lang = detect_lang(text)
    msg = "result : " + lang
show_form(text, msg)
