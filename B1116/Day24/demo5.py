import openpyxl


workbook=openpyxl.load_workbook('./../data/Book2.xlsx')

sheet=workbook['Sheet1']

for i in range(1,4):
    for j in range(1,4):
        v=sheet.cell(i,j).value
        print(v)


workbook.close()
