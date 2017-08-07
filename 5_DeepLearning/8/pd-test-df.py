import pandas as pd

a = pd.DataFrame([
    [10, 20, 30],
    [40, 50, 60],
    [100, 200, 300]
])
#print(a)

b = pd.Series([1.0, 3, 5.0, 10])
#print(b)

#   키, 몸무게, 유형 데이터프레임 생성
tbl = pd.DataFrame({
    "weight" : [80.0, 70.4, 65.5, 45.9, 51.2],
    "height" : [170, 190, 155, 140, 155],
    "gender" : ["f,", "m", "f", "f", "m"]
})

#   몸무게 목록 추출
#print("weight = \n", tbl["weight"])

#print("weight, height = \n", tbl[["weight", "height"]])

#print("3. tbl[2:4]\n", tbl[2:4])

#print("4. tbl[3:]\n", tbl[3:])

#print("5. height > 160 : ", tbl[tbl.height >= 160])

#print("6. gender : \n", tbl[tbl.gender == "m"])

print("7, sort by heigh\n", tbl.sort_values(by="height"))

print("8. sort by weight\n", tbl.sort_values(by="weight", ascending=False))