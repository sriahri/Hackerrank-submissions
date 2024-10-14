# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    s=input()
    try:
        re.compile(s)
        print('True')
    except re.error:
        print('False')
