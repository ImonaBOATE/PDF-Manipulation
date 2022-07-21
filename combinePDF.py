# Importing in the following libraries
import PyPDF2 # manipulates PDFs
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        merger.append(file)
        print(file)
# creating the new combined PDF file and storing it in the current folder
merger.write('combined.pdf')





