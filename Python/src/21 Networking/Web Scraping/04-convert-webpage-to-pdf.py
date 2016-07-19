import ho.pisa as pisa
import urllib

# Pisa has the following dependencies
# 1) ReportlabToolkit 2.1+ (required)
# 2) html5lib 0.10+ (required)
# 3) pyPdf 1.11+ (optional)
# 4) PIL 1.1.6+ (optional)


def create(data, filename):
    f = file(filename, 'wb')
    pdf = pisa.CreatePDF(data, f)
    f.close()
    if not pdf.err:                             
        pisa.startViewer(filename)                

url = "http://www.artima.com/pins1ed/first-steps-in-scala.html"

# create 2 PDFs - from a webpage and a simple string
create(urllib.urlopen(url).read(), "webpage.pdf")
create("Hello <strong>World</strong>", "hello.pdf")

1
