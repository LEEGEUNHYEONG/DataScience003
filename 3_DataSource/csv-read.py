import codecs

#   EUC_KR  CSV 파일 읽기
filename = "list-euckr.csv"

#   read 1
csv = codecs.open(filename, "r", "euc_kr").read()

#   csv -> python
data = []
rows = csv.split("\r\n")
for row in rows :
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)

#   출력
for c in data:
    print(c[0], c[1], c[2])


"""
#   read2, 에러 출력
import csv
fp = codecs.open(filename, "r", "shift_jis")

#   한줄씩 읽기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
"""