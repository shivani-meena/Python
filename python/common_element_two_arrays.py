a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
p = []
flag = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i] == b[j]:
            k = 0
            while k < len(p):
                if p[k] == a[i]:
                    flag = 1
                k += 1
            if flag == 0:
                p.append(a[i])
        j += 1
    i += 1
if len(p) != 0:
    print(*p)
else:
    print("No")
























