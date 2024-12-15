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



# a = [7, 5, 9, 2, 8]
# i = 0
# while i < len(a)-2:
#     j = i 
#     mini = i
#     while j < len(a)-1:
#         if a[j] < a[mini]:
#             mini = j 
#         j += 1 
#     a[i], a[mini] = a[mini], a[i]
#     i += 1
# print(a)
