a = list(map(int, input().split()))
i = 0
flag = True
while i < len(a):
    if a[i] < 0:
        flag = True
        break
    else:
        flag = False
    i += 1
if flag == True:
    print("Yes")
else:
    print("No")

