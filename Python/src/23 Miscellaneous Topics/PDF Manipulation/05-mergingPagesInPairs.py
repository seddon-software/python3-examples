from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import math

def main():
    inFile = "pdfs/OFT1364.pdf"
    outFile = "pdfs/OFT1364-with-pages-merged-in-pairs.pdf"
    input = PdfFileReader(open(inFile, "rb"))
    output = PdfFileWriter()
    
    inch = 72
    h = horizontal = 8.5 * inch
    v = vertical = 11 * inch

    for page in range (0, input.getNumPages(), 2):
        lhs = input.getPage(page+1)
        lhs.scaleTo(h/2, v/2)
        try: 
            rhs = input.getPage(page)
            rhs.scaleTo(h/2, v/2)
            lhs.mergeTranslatedPage(rhs, h/4, v/2, True)
        except: 
            pass   # if the PDF has an odd number of page, you can't merge on the last page
        output.addPage(lhs)
        print (str(page) + " "),
        sys.stdout.flush()

    print("writing ")
    outputStream = file(outFile, "wb")
    output.write(outputStream)
    print("done.")

if __name__ == "__main__":
    main()
