n = int(input())
i = 3
sum = 0
c = 0
while True:
    sum += i
    print(i,end=" ")
    c += 1
    if c == n:
        break
    i += 2
print("sum",sum)
