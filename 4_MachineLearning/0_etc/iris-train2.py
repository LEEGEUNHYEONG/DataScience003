import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

#   CSV 파일 읽기
csv = pd.read_csv('iris.csv')

#   열 추출
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]

#   학습, 테스트 데이터 나누기
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

#   학습 및 예측
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

#   출력
as_score = metrics.accuracy_score(test_label, pre)
print("정답률 = ", as_score)

