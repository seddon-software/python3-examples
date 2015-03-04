from PyPDF2 import PdfFileWriter, PdfFileReader

filename = "pdfs/OFT1364.pdf"
pdf = PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print page.extractText()
    
