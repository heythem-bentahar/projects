from PyPDF2 import *
from pathlib import *

class merger():

    def __init__(self):
        pass

    def merge(self, path):
        path = Path(str(path))
        pdf_pth = [str(p) for p in path.glob("*")]
        merger = PdfFileMerger()
        for p in sorted(pdf_pth):
            if not p.endswith("Merged.pdf"):
                merger.append(p)

        def m():
            with open (path/ "Merged.pdf","wb") as file:
                    merger.write(file)
                    file.close()
            
        if (path/ "Merged.pdf").exists():
            print("\nYou want to delet 'Merged.pdf' first (Y/n):")
            n = str(input())
            if n == ("Y") or n ==("y"):
                m()
                print("Merge Completed...")
            elif n == ("n") or n== ("N"):
                print("OK, Pleas rename your file an try again.")
        else:
                m()
                print("Merge Completed...")

path = input("Enter the path of the PDF's:\n")

g = merger()
g.merge(path)