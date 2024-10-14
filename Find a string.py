def count_substring(string, sub_string):
    i=0
    c=0
    while string.find(sub_string,i)!=-1:
        c+=1
        i=string.find(sub_string,i)+1
    return c