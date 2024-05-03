a = list(map(int, input().split())) 
n = int(input())
i = 0
flag = 0
while i < len(a):
    if a[i] == n:
        flag = 1
        break
    else:
        flag = 0
    i += 1
if flag == 1:
    print("Yes")
else:
    print("No")
    
