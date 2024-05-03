a = list(map(int, input().split()))
k = int(input())
i = 0
flag = 0
p = 0
while i < len(a):
    if a[i] > k:
        p = a[i]
        flag = 1
        break
    i += 1
if flag == 1:
    print(p)
else:
    print("no")
