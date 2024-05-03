a = [14, 33, 27, 35, 10]
n = len(a)
i = 0
while i < n - 1:
    j = 0
    while j < n - ( i + 1):
        if a [ j ] > a [ j + 1 ]:
            a [ j ] , a [ j + 1 ] = a [ j + 1 ] , a [ j ]
        j += 1 
    i += 1
print(a)


i = 0
j = 0 to 8
i = 1
j = 0 to 7 
i = 2
j = 0 to 6
i = 8 
j = 0 to 0 
