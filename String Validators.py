s = input()
for i in s:
    if i.isalnum():
        print('True')
        break
else:
    print('False')
for j in s:
    if j.isalpha():
        print('True')
        break
else:
    print('False')
for k in s:
    if k.isdigit():
        print('True')
        break
else:
    print('False')
for l in s:
    if l.islower():
        print('True')
        break 
else:
    print('False')
for m in s:
    if m.isupper():
        print('True')
        break
else:
    print('False')
