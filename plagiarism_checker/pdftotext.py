from browse import search_for_file_path
import PyPDF2
from extchange import extchange
from checkfiles import checkfiles
def pdftotxt():
    a = checkfiles()
    
    for i in a:
        file = i.split('/') 
        b = PyPDF2.PdfFileReader(i)
        str = ""
        c = b.getNumPages()
        for j in range(1, c):
            str += b.getPage(j).extractText()
        with open(extchange(file[-1]), "w", encoding="CP1252") as f:
            f.write(str)
