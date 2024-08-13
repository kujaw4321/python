from PyPDF2 import PdfWriter

writer = PdfWriter()

writer.add_blank_page(width=72 * 8.5, height = 72 * 11)

with open("outputpdf.pdf", "wb") as output_pdf:
    writer.write(output_pdf)