def swap_case(s):
    r=""
    for i in s:
        if i==i.upper():
            r+=i.lower()
        else:
            r+=i.upper()
    return r