def is_isogram(string):
    check=True
    string=string.lower()
    for i in string:
        if i!=" " and i!="-" and string.count(i)>1:
            check=False
            break

    return check
