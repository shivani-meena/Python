a = list(map(int, input().split()))
i = 0
odd_count = 0
while i < len(a):
    if a[i] % 2 != 0:
        odd_count += 1
    i += 1
print(odd_count)
        
