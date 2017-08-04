from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

#   파일 읽기
tbl = pd.read_csv("bmi.csv")

#   정규화
label = tbl["label"]
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w, h], axis = 1)

#   학습 & 테스트 데이터 구분
data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)

#   데이터 학습
clf = svm.SVC()
clf.fit(data_train, label_train)

#   데이터 예측
predict = clf.predict(data_test)

#   결과 테스트
as_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("정답률 :", as_score)
print("리포트 =\n", cl_report)