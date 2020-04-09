def is_valid(isbn):
    num = []
    isbn = isbn.replace('-','')
    if isbn=='' or len(isbn)<10:return False
    print(isbn)
    for i in isbn:
        if i in '0123456789':
            num.append(int(i))
        elif i=='X':
            if len(num)==9:
                num.append(10)
            else:
                return False
        else:
            return False  
    if len(num)>10:return False
    return sum(map(lambda x:x[0]*x[1],enumerate(num,1)))%11==0