n = int(input()) 
i = 1
while i <= n:
    j = 1 
    while j <= i:
        print("*",end="") 
        j += 1 
    i += 1
    print()
