from PyPDF2 import PdfFileWriter, PdfFileReader

inputFile = "pdfs/OFT1364.pdf"
outputFile = "out/OFT"

input = PdfFileReader(file(inputFile, "rb"))


for page in range(0, input.getNumPages()):
    output = PdfFileWriter()
    output.addPage(input.getPage(page))
    outFileName = "{0}{1:02}.pdf".format(outputFile, page)
    print outFileName
    outputStream = file(outFileName, "wb")
    output.write(outputStream)
    outputStream.close()    

for page in range(0, input.getNumPages()):
    inFileName = "{0}{1:02}.pdf".format(outputFile, page)
    outFileName = "{0}{1:02}.txt".format(outputFile, page)
    print outFileName
    input = PdfFileReader(file(inFileName, "rb"))
    f = open(outFileName, "w")
    f.writelines(input.getPage(0).extractText())
    f.close()

