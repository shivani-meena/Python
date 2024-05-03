arr = [15, 4, 45, 13, 6, 2, 3, 8]
i = 0
while i < len(arr):
    j = i
    while j > 0:
        if  arr [ j ] < arr [ j - 1 ] :
            arr [ j - 1] , arr [ j ]  =  arr [ j ] , arr [ j - 1] 
        j -= 1 
    i += 1 
print(arr)

