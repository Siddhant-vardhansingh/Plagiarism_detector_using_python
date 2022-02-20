def extchange(string):
    d = list(string)
    e = len(d)
    d[e-3:] = ['t', 'x', 't']
    str1 = ""
    for k in d:
        str1 += k
    return str1