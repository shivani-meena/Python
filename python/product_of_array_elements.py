a = list(map(int, input().split()))
i = 0
product = 1
while i < len(a):
    product = product*a[i]
    i += 1
print(product)

