def wrap(string, max_width):
    s=''
    i=0
    while(i<=len(string)):
        s+=string[i:i+max_width]+'\n'
        i+=max_width
    return s
    
        