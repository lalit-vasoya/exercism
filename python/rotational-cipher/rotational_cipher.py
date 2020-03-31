def rotate(text, key):
    temp=""
    for i in text:
        d=ord(chr(ord(i)+key))
        
        if i.isalpha() and i.isupper():
            if d>90:
                d=(d-90)+64
            temp+=chr(d)

        elif i.isalpha():
            if d>122:
                d=(d-122)+96
            temp+=chr(d)

        else:
            temp+=i
    
    return temp
