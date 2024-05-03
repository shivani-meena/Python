a = [2, 6, 8, 5]
i = 0
sum1 = 0
while i < len(a): 
    j = i
    sum2 = 0
    while j < len(a):
        sum2 += a[j]
        sum1 += sum2 
        j += 1
    i += 1 
print(sum1)
