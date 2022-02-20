import os
import difflib

from pdftotext import pdftotxt
def pdf_similarity():
    
    first_file_list = [_ for _ in os.listdir() if _.endswith('txt')]
    first_file = first_file_list[0]
    second_file = first_file_list[1]
    first_file_lines = open(first_file).readlines()
    second_files_lines = open(second_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, second_files_lines, first_file, second_file)
    differnce_report = open(r"C:\Users\HP\Documents\mini-project\Plagiarism_detector_using_python\plagiarism_checker\report.html",'w')
    differnce_report.write(difference)
    differnce_report.close()

