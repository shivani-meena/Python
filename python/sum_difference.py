a = list(map(int, input().split()))
i = 0
sum = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        sum += abs(a[i] - a[j])
        j += 1 
    i += 1
print(sum)
        
