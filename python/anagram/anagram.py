def find_anagrams(word, candidates):
    len_word         = len(word)
    candidates = list(filter(lambda x:len(x)==len_word,candidates)) # filter to select exact length word 
    output_list = candidates.copy()

    for item in candidates: 
        for letter in word.lower(): 
            if letter not in item.lower():
                #when letter not match in item
                if item in output_list:output_list.remove(item)
                break
            elif item.lower().count(letter)!= word.lower().count(letter):
                # when letter match in item but not exact word
                if item in output_list:output_list.remove(item)
                break

    # remove all duplicate in same list
    temp_list =  output_list.copy()     
    for i in range(0,len(temp_list)):
        if word.lower()==temp_list[i].lower():      
            output_list.remove(temp_list[i])

    return output_list

        
