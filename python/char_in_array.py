str=input()
s=input() 
i=0
flag=0
while i<len(str):
    if str[i]==s:
        flag=1
        break
    else:
        flag=0
    i+=1 
if flag==1:
    print("Yes")
else:
    print("No")


