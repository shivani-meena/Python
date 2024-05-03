a = list(map(int, input().split()))
i = 0
sum = 0
while i < len(a):
    if a[i] == 0:
        break
    sum += a[i]
    i += 1 
print(sum)
