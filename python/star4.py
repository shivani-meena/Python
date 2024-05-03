n = int(input())
i = 1
while i <= n*2:
    j = 1
    while j <= n*2 - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= i:
        print("*", end="")
        k += 1
    i += 2
    print()
