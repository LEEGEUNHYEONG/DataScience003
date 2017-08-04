#   Grid search 관련 내부 에러 발생, 정상동작 하지 않음
import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.grid_search import GridSearchCV

#   MNIST 학습 데이터 읽기
train_csv = pd.read_csv("./mnist/train.csv")
test_csv = pd.read_csv("./mnist/t10k.csv")

#   열 추출
train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:577]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:577]
print("학습 데이터 수 = ", len(train_label))

#   그리드 서치 매개변수 설정
params = [
    {"C":[1, 10, 100, 1000], "kernel":["linear"]},
    {"c":[1, 10, 100, 1000], "kernel":["rbf"], "gamma":[0.001, 0.0001]}
]

#   그리드 서치 수행
clf = GridSearchCV(svm.SVC(), params, n_jobs= -1)
clf.fit(train_data, train_label)
print("학습기=", clf.best_estimator_)

#   확인
pre = clf.predict(test_data)
as_score = metrics.accuracy_score(pre, test_label)
print("정답률=", as_score)

