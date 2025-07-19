# This code will create a new PDF file 'newfile.pdf' containing only the specified pages from 'source.pdf'.
# Note: Make sure to install PyPDF2 using pip if you haven't already:

from PyPDF2 import PdfWriter, PdfReader
pages_to_keep = [0, 2, 4, 6] # page numbering starts from 0
infile = PdfReader('source.pdf', 'rb')
output = PdfWriter()

for i in pages_to_keep:
    p = infile.pages[i] 
    output.add_page(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)