a = list(map(int, input().split()))
i=0
max=0
while i<len(a):
    j=i+1 
    count=1
    while j<len(a):
        if a[i]==a[j]:
            count+=1 
        if count>max:
            max=count
            p=a[i]
        j+=1
    i+=1
print(p)
