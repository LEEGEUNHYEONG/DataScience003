import openpyxl

#   엑셀파일 열기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

#   시트 추출
sheet = book.active

#   서울을 제외한 인구 구하기
for i in range(0, 10) :
    #   왜 66을 더하는건가 ???
    year = int(sheet[str(chr(i + 66)) + "2"].value)
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print(year, "서울 제외 인구 : " , output)

    #   쓰기
    sheet[str(chr(i+66)) + "21"] = output
    cell = sheet[str(chr(i+66)) + "21"]
    #   폰트, 색상 변경
    cell.font = openpyxl.styles.Font(size=10, color="FF0000")
    cell.number_format=cell.number_format


#   엑셀 파일 저장
filename = "population.xlsx"
book.save(filename)
print("ok")
