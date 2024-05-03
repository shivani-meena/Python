a = list(map(int, input().split()))
i = 0
while  i < len(a):
    j = 0
    sum = 0
    while j < len(a):
        if i != j:
            sum = sum + a [ j ]
        j += 1 
    print(sum, end=" ") 
    i += 1

