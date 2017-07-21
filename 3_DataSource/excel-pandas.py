#   pandas 설치
#   pip3 install pandas
#   pip3 install xlrd

import pandas as pd

#   엑셀 파일 열기
filename = "stats_104102.xlsx"
sheet_name = "stats_104102"
book = pd.read_excel(filename, sheetname=sheet_name, header=1)

#   2016 인구순 정렬
#   2007 ~ 2012 는 에러 출력 됨, 세종 - 때문
book = book.sort_values(by=2016, ascending=False)
print(book)