#   Python - Excel 설치
#   pip3 install openpyxl
import openpyxl

#   엑셀 파일 열기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

#   시트 추출
sheet = book.worksheets[0]

#   시트의 각 행 추출
data = []
for row in sheet.rows:
    data.append([
        row[0].value,   #   시트의 계 column
        row[10].value   #   시트의 2016 column
    ])

#   필요없는 줄 제거
del data[0]     #   title row, 시도별~
del data[1]     #   년도 row
del data[2]     #   계 row

#   데이터를 인구 순서로 정렬
data = sorted(data, key=lambda x:x[1])

#   하위 5 출력
for i, a in enumerate(data) :
    if(i >= 5) : break
    print(i+1, a[0], int(a[1]))