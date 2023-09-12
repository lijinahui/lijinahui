from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
print(sheet.title)
sheet.title = "Alex大王的姑娘们"
shee
wb.save("execl_test.xlsx")

