def grep(pattern, flags, files):
    n,l,i,v,x  = '-n' in flags,'-l' in flags,'-i' in flags,'-v' in flags,'-x' in flags
    pattern = pattern.lower() if i else pattern 
    print(pattern)
    m = len(files)>1
    result = ''
    for file in files:
        for line_num,line_text in enumerate(open(file).readlines(),1):
            line = line_text.lower() if i else line_text              
            if v ^ (pattern+'\n'==line if x else pattern in line):
                if l: result+= file+"\n"; break; 
                result += (f"{file}:" if m else '') + (f"{line_num}:" if n else '') + line_text

    return result