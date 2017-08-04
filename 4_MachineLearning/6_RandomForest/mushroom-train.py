import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#   데이터 읽기
mr = pd.read_csv("mushroom.csv")

#   데이터 내부 기호를 숫자로 변환
label = []
data = []
attr_list = []

for row_index, row in mr.iterrows() :
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:] :
        row_data.append(ord(v))
    data.append(row_data)


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