a = list(map(int, input().split()))
i = 0
max = 0
c = 1
while i < len(a) - 1:
    if a[i] - a[i+1] <= 0:
        c += 1 
    else:
        if c > max:
            max = c
        c = 1
    i += 1 
if c > max:
    max = c
print(max)
