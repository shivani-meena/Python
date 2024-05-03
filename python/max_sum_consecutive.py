a = list(map(int, input().split()))
i = 0
max_sum = 0
while i < len(a)-1: 
    if a[i] + a[i+1] > max_sum:
        max_sum = a[i] + a[i+1]
    i += 1
print(max_sum)
