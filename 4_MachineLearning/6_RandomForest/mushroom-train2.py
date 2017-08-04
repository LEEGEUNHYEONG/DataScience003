import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#   데이터 읽기
mr = pd.read_csv("mushroom.csv")

#   데이터 내부의 분류 변수 전개
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows() :
    label.append(row.ix[0])
    exdata = []

    for col, v in enumerate(row.ix[1:]) :
        if row_index == 0 :
            attr = {"dic":{}, "cnt":0}
            attr_list.append(attr)
        else :
            attr = attr_list[col]

        #   버섯의 특징 기호를 배열로 나타내기
        d=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if v in attr["dic"] :
            idx = attr["dic"][v]
        else :
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

#   학습 & 테스트 데이터 구분
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

#   데이터 학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

#   데이터 예측
predict = clf.predict(data_test)

#   출력
as_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 = ", as_score)
print("리포트 =\n", cl_report)