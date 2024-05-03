s=input()
n=int(input())
i=0
str=" "
while i<len(s):
    if i!=n:
        str+=s[i] 
    else:
        str+=s[i].upper() 
    i+=1
print(str)
