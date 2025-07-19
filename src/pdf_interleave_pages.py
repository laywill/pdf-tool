# This code will create a new PDF file 'newfile.pdf' containing interleaved pages from 'Taskmaster_Inside.pdf' and 'Taskmaster_Outside.pdf'.
# Note: Make sure to install PyPDF2 using pip if you haven't already:
# pip install PyPDF2

from PyPDF2 import PdfWriter, PdfReader

infile_odd = PdfReader('Taskmaster_Outside.pdf', 'rb')
infile_even = PdfReader('Taskmaster_Inside.pdf', 'rb')
output = PdfWriter()

# Confirm both PDFs have the same number of pages
if len(infile_odd.pages) != len(infile_even.pages):
    raise ValueError("Both PDFs must have the same number of pages.")

# Interleave pages from both PDFs
for i, (odd_page, even_page) in enumerate(zip(infile_odd.pages, infile_even.pages)):
    output.add_page(odd_page)  # Add odd page first
    output.add_page(even_page)  # Then add even page

# Write the interleaved pages to a new PDF file
with open('newfile.pdf', 'wb') as f:
    output.write(f)
