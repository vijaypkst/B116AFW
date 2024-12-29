import openpyxl

class Utility:
    @staticmethod
    def get_xldata(xl_path,sheet_name,row,col):
        try:
            wb=openpyxl.load_workbook(xl_path)
            sheet=wb[sheet_name]
            value=sheet.cell(row,col).value
            if value==None:
                print('cell value is None')
                value=''
        except Exception as e:
            print(str(e))
            value = ''

        return value
