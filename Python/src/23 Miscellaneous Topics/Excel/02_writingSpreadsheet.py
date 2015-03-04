from xlwt import Workbook


book = Workbook()
sheetA = book.add_sheet('A')
sheetB = book.add_sheet('B')

sheetA.write(0, 0, 'Monday')
sheetA.write(1, 1, 'Tuesday')
sheetA.write(2, 2, 'Wednesday')
sheetA.write(3, 3, 'Thursday')
sheetA.write(4, 4, 'Friday')

for row in range(3, 10):
    for col in range(5, 10):
        sheetB.write(row, col, 'X')

book.save('books/Book2.xls')
