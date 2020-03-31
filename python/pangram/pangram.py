def is_pangram(sentence):
    check=True
    sentence=sentence.lower()
    for i in range(97,123):
        if chr(i) not in sentence:
            check=False
            break
        
    return check
