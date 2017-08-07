import pandas as pd

tbl = pd.DataFrame([
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
])

#print(tbl)

#   행 / 열 반전
print(tbl.T)