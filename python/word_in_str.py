import re
str1 = input().lower()
w = input().lower()
p = r'[^\w\s]'
rep_char = ""
s = re.sub(p, rep_char, str1)
i = 0
flag = 1
k = s.split() 
print(k,s)
while i < len(k):
    if k[i] == w:
        flag = 1
        break
    else:
        flag = 0
    i += 1
if flag == 1:
    print("Yes")
else:
    print("No")
