def abbreviate(words):
    return "".join([i[0].upper() for i in words.replace("_" ,"").replace("-"," ").split()])


