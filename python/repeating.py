a=[10, 3, 2, 3, 5, 6,5,2]
i=0
arr=[]
while i<len(a)-1:
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            k=a[i]
            arr.append(a[i])
        j+=1
    i+=1  
print(arr[0])
