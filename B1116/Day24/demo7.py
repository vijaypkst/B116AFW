import  openpyxl


workbook=openpyxl.load_workbook('./../data/Book1.xlsx')
sheet=workbook['Sheet1']
sheet['A1'].value='Bhanu'
workbook.save('./../data/Book1b.xlsx')
workbook.close()
