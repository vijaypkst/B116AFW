import  openpyxl

#open the xl file
workbook=openpyxl.load_workbook('./../data/Book1.xlsx')
#go to sheet1
sheet=workbook['Sheet1']
#v=sheet['A1'].value or
v=sheet.cell(1,1).value
print(v)
workbook.close()
