from pathlib import *
from PyPDF2 import *

class pdf_spliter():


    def __init__(self, path):

        self.path = Path(str(path))
        
    def split(self, break_p):

        self.break_p = int(break_p)
        pdf =  PdfFileReader(self.path) 
        self.writer1 = pdf.pages[:break_p]
        self.writer2 = pdf.pages[break_p:]
        

    def writer(self, filname):
        self.filname1 = Path(f"{self.path.parent}/{filname}_1.pdf")
        self.filname2 = Path(f"{self.path.parent}/{filname}_2.pdf")

        writer1 = PdfFileWriter()
        writer2 = PdfFileWriter()
        for page in self.writer1:
            writer1.addPage(page)
        for page in self.writer2:        
            writer2.addPage(page)

        with open (self.filname1, "wb") as file:
            writer1.write(file)
            
        with open (self.filname2, "wb") as file:
            writer2.write(file)

pdf = str(input("Enter The PDF to split:\n"))
split = int(input("Enter your split number\n"))
new_pdf = str(input("Enter The New PDF name (e.g: new_file ===> new_file1 | new_file2):\n"))

pdf = pdf_spliter(rf"{pdf}")
pdf.split(split)
pdf.writer(new_pdf)