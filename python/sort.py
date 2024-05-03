a=[15, 23, 16] 
i=0
b=[]
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1 
print(a)

    
        

