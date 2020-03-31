def decode(s):

    temp=""
    ans=""
    for i in s:     
        if i.isnumeric():
            temp+=i
        else:
            if temp.isnumeric():
                ans+=i*int(temp)
                temp=""
            else:
                ans+=i
    print(ans)
    return ans

def encode(string):
    
    temp=""

    if len(string)>0:
        pre=string[0]
    else:
        return ""
    cnt=0

    for i in string:
        if i!=pre:
           
            print(temp)
            print(i) if pre==" " else ""
            temp+=str(cnt)+pre if cnt!=1 else pre
            pre=i
            cnt=1
        else:
            cnt+=1
    
    temp+=str(cnt)+pre if cnt!=1 else pre
            

    return temp
        
#encode("  hsqq qww  ")
decode("2a3b4c")

