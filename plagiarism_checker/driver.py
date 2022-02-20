from pdf_similarity import pdf_similarity
from pdftotext import pdftotxt
from similarity import similarity
import webbrowser

input_var = int(input("Press 1 to deal with PDF file \nPress 2 to deal with text files \n"))
if (input_var == 1):
    pdftotxt()
    pdf_similarity()
    filename = r"C:\Users\HP\Documents\mini-project\Plagiarism_detector_using_python\plagiarism_checker\report.html"
    webbrowser.open_new_tab(filename)
elif (input_var == 2):
    similarity()
    filename = r"C:\Users\HP\Documents\mini-project\Plagiarism_detector_using_python\plagiarism_checker\report.html"
    webbrowser.open_new_tab(filename)
else:
    print("INVALID")

