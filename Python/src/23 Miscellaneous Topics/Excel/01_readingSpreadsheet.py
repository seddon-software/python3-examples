from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

workbook = "books/Book1.xls"
print open_workbook(workbook)
with open(workbook,'rb') as f:
    print open_workbook(
        file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
        )
aString = open(workbook,'rb').read()
print open_workbook(file_contents=aString)

wb = open_workbook(file_contents=aString)
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
    print
