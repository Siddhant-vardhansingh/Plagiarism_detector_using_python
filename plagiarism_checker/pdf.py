import PyPDF2
import os
def checkfiles():
    path = r"C:\Users\HP\Documents\mini-project\plagiarism_checker"
    l = os.listdir(path)
    list = []
    for files in l:
        length = len(files)
        files2 = files[length - 3:]
        if files2 == 'pdf':
            list.append(files)
    return list

def extchange(string):
    d = list(string)
    e = len(d)
    d[e-3:] = ['t', 'x', 't']
    str1 = ""
    for k in d:
        str1 += k
    return str1
        

def pdftotxt():
    a = checkfiles()
    for i in a: 
        b = PyPDF2.PdfFileReader(i)
        str = ""
        c = b.getNumPages()
        for j in range(1, c):
            str += b.getPage(j).extractText()
        with open(extchange(i), "w", encoding="CP1252") as f:
            f.write(str)

pdftotxt()