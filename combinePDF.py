# Importing in the following libraries
import PyPDF2 # manipulates PDFs
import os


for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        PyPDF2.PdfFileMerger().append(file)
    # creating the new combined PDF file and storing it in the current folder
    PyPDF2.PdfFileMerger().write('combined.pdf')





