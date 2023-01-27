import os
import tkinter as tk
from tkinter import filedialog
import PyPDF2
from PyPDF2 import PdfMerger
import classfile as s

root = tk.Tk()
root.withdraw()

pdf_files = []

for i in range(2):
    filepath = filedialog.askopenfilename(title="Select pdf file", filetypes=[("PDF files", "*.pdf")])
    pdf_files.append(filepath)

try:
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(open(pdf, 'rb'))
    with open('merged_pdf.pdf', 'wb') as fout:
        merger.write(fout)
    merger.close()
    print("Successfully merged the PDF files.")

    pdf_file = "merged_pdf.pdf"
    watermark = "wmark1.pdf"
    merged_file = "me.pdf"

    input_file = open(pdf_file,'rb')
    input_pdf = PyPDF2.PdfReader(input_file)

    watermark_file = open(watermark,'rb')
    watermark_pdf = PyPDF2.PdfReader(watermark_file)

    pdf_page = input_pdf.pages[0]

    watermark_page = watermark_pdf.pages[0]

    pdf_page.merge_page(watermark_page)

    output = PyPDF2.PdfWriter()

    output.add_page(pdf_page)

    merged_file = open(merged_file,'wb')
    output.write(merged_file)

    merged_file.close()
    watermark_file.close()
    input_file.close()
except Exception as e:
    s.mergeme(pdf_name='watermark_pdf')
    print("Error: ",e)

