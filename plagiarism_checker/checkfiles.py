import os

def checkfiles():
    path = r"C:\Users\HP\Documents\mini-project\Plagiarism_detector_using_python\plagiarism_checker"
    l = os.listdir(path)
    list = []
    for files in l:
        length = len(files)
        files2 = files[length - 3:]
        if files2 == 'pdf':
            list.append(files)
    return list