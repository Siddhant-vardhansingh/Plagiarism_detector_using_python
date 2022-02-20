import difflib
from browse import search_for_file_path


def similarity():
    first_file = search_for_file_path()
    second_file = search_for_file_path()
    first_file_lines = open(first_file).readlines()
    second_files_lines = open(second_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, second_files_lines, first_file, second_file)
    differnce_report = open(r'C:\Users\HP\Documents\mini-project\Plagiarism_detector_using_python\plagiarism_checker\report.html','w')
    differnce_report.write(difference)
    differnce_report.close()