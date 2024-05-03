a = list(map(int, input().split()))
i = 0
min = abs(a[0]-a[1])
max = 0
while i < len(a):
    j = 0
    while j < len(a):
        if i != j:
            if a[i] - a[j] > max:
                max = a[i] - a[j]
            if a[i] - a[j] < min and a[i] - a[j] >= 0:
                min = a[i]-a[j]
        j += 1 
    i += 1 
print(max)
print(min)
