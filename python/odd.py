n=int(input())
i=1
c=0
while True:
    if i%2!=0:
        print(i)
        c+=1 
        if c==n:
            break
    i+=1
