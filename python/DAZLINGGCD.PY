t=int(input())
for i in range(t):
    x,y= map(int,input().split())
    if x%2==0:
        if x+2<=y:
            print(x,x+2)
        else:
            print(-1)
    elif x%3==0:
        if x+3<=y:
            print(x,x+3)
        else:
            print(-1)
    else:
        if x+3<=y:
            print(x+1,x+3)
        else:
            print(-1)
            
