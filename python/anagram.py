a="New York Time"
b="monkeys write"
r=a.lower()
s=b.lower()
r=r.replace(" ", "")
s=s.replace(" ", "")

i=0
count=0
while i<len(r):
    j=0
    while j<len(s):
        if r[i]==s[j]:
            count+=1 
        j+=1 
    i+=1 
if count==len(a):
    print("yes")
else:
    print("no")
    
        
