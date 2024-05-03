n = int(input())
count = 0
i = 2
while True:
    j = 2
    c = 0
    while j < i:
        if i % j == 0:
            c += 1
        j += 1
    if c == 0: 
        count += 1
        print(i, end=" ")
        if count == n:
            break
    i += 1

