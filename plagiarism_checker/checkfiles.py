import os

from browse import search_for_file_path

def checkfiles():
    file1 = search_for_file_path()
    file2 = search_for_file_path()
    list = []
    list.append(file1)
    list.append(file2)
    

    list2 = []
    for files in list:
        length = len(files)
        files2 = files[length - 3:]
        if files2 == 'pdf':
            list2.append(files)
    return list2