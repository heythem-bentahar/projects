from pathlib import *
from PIL import Image

# path input #

path = input("Enter The path of you Images directory: \n")
path = Path(f"{path}")

####################################################
# making a subdirectory to contain the PDF version #

(path/"PDF's").mkdir(exist_ok=True) 

# iterating over every file in the given directory #
# we use try function to ignore non image files #

for pp in path.glob("*"):
    try: 
        with Image.open(pp) as image:
            im = image.convert("RGB")
            pth = Path(f"{path}\PDF's\{pp.stem}.pdf")
            im.save(pth, save_all=True)
    except:
        pass

print("Conversion Completed ...")