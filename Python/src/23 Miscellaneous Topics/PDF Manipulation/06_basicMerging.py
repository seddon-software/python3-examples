from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
     
input1 = open("pdfs/Constants.pdf", "rb")
input2 = open("pdfs/Events.pdf", "rb")
input3 = open("pdfs/Functions.pdf", "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj = input1, pages = (0,1))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position = 2, fileobj = input2, pages = (0,1))

# append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("pdfs/ConstantsEventFunctions-merged.pdf", "wb")
merger.write(output)
