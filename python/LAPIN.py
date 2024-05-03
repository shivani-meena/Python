t=int(input())
for i in range(t):
    s=input()
    if len(s)%2==0:
        a=len(s)//2
        b=sorted(s[:a])
        c=sorted(s[a:])
        if b==c:
            print("YES")
        else:
            print("NO")
    else:
        a=len(s)//2
        b=sorted(s[:a])
        c=sorted(s[a+1:])
        if b==c:
            print("YES")
        else:
            print("NO")
       
        
