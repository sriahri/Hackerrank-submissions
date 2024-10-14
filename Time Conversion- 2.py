s=input()
if("PM" in s):
    r=list(s.split("PM"))
else:
    r=list(s.split("AM"))
l= list(r[0].split(":"))
if("PM" in s):
    if int(l[0])!=12:
        l[0]=str(int(l[0])+12)
if 'AM' in s:
    if int(l[0])==12:
        l[0]=str('00')
se=str(l[0])+":"+l[1]+":"+l[2]
print(se)
