arr = [1, 2, 3, 5]
i = 0
while i < len(arr):
    j = i
    b = []
    while j < len(arr):
        b.append( arr[ j ])
        print(*b)
        j += 1 
    i += 1 
