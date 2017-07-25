import pandas as pd
from sklearn import svm, metrics

#   XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

#   학습데이터, 전용데이터 분류
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0 : 1]  # 데이터
xor_label = xor_df.ix[:,2]      # 결과

#   학습 및 예측
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

#   출력
as_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = " , as_score)