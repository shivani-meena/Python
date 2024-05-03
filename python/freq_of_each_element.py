a = list(map(int, input().split()))
i=0
p=[]
d={}
while i<len(a):
    j=i
    count=0
    flag=0
    while j<len(a):
        if a[i]==a[j]:
           count+=1
        j+=1
    k=0
    while k<len(p):
         if p[k]==a[i]:
             flag=1
         k+=1
    if flag==0:
        p.append(a[i])
        d[a[i]]=count
    i+=1
for j in d:
    print(j, d[j])


            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   
   
   
   
   
               
