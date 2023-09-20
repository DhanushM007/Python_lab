from PyPDF2 import PdfReader,PdfWriter
num1=int(input("enter page no from pdf1"))
num2=int(input("enter page no from pdf2"))
pdf1=open("C:\\Users\\jaswa\\Desktop\\JASHU MBA PAYMENT PDF.pdf","rb")
pdf2=open("C:\\Users\\jaswa\\Desktop\\DARSHAN MBA PAYMENT PDF.pdf","rb")
pdf_writer=PdfWriter()
pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num1-1]
pdf_writer.add_page(page)

pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num2-1]
pdf_writer.add_page(page)

with open("C:\\Users\\jaswa\\Desktop\\new1.pdf","wb") as output:
    pdf_writer.write(output)
print("combined successfully")
    

