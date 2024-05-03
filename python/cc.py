a=[1,2,3,4,5,6,7,8]
i=0
k=[]
sum=0
while i<len(a):
    s=a[i]+a[i+1] 
    k.append(s)
    i+=2 
print(k)

