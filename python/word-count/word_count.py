import re
def count_words(sentence):
    sentence=sentence.lower()

    sentence=re.sub("[^a-z0-9'\s{1}]|[^a-z]'|'[^a-z]|\t|\n|'$"," ",sentence).strip()
    
    sentence=re.sub(r"\s{2,}"," ",sentence)

    out={}
    temp=re.split(' ',sentence)
    for i in temp:
        out[i]=temp.count(i)
    
    return out

