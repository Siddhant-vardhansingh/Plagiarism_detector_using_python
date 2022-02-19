import os
def checkfiles():
    path = r"C:\Users\HP\Documents\mini-project\plagiarism_checker"
    l = os.listdir(path)
    print(l)
    list = []
    for files in l:
        length = len(files)
        files2 = files[length - 3:]
        if files2 == 'pdf':
            list.append(files)
    return list
checkfiles()