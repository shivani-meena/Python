a = list(map(int, input().split()))
i=0
flag=0
while i<len(a)-1:
    if a[i]-a[i+1]<0:
        flag=1
    else:
        flag=0
        break 
    i+=1 
if flag==1:
    print("yes")
else:
    print("no")
