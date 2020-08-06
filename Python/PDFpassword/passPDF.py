from PyPDF2 import PdfFileReader, PdfFileWriter

pdfwriter = PdfFileWriter()

pdf = PdfFileReader("TAHA_Solution.pdf")
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))

password = "Omnissiah"
pdfwriter.encrypt(password)

with open("TAHA_Solution_encrypted.pdf",'wb') as f:
    pdfwriter.write(f)
    f.close()