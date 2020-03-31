def score(word):
    letval={"AEIOULNRST":1,"DG":2,"BCMP":3,"FHVWY":4,"K":5,"JX":8,"QZ":10}
    word=word.upper()
    s=0
    for i in word:
        for j in letval:
            if i in j:
                s+=letval[j]
                break
        
    return s
