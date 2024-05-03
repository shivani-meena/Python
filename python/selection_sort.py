arr = [5, 2, 6, 7, 2, 1, 0, 3]
i = 0
while i < len(arr) - 1:
    j = i
    min_index = i
    while j < len(arr):
        if arr [ j ] < arr [min_index]:
            min_index = j 
        j += 1 
    arr [ i ] , arr [ min_index ] = arr [ min_index ] , arr [ i ]
    i +=1 
print(arr)

