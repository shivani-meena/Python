a = int(input())
b = int(input()) 
max1 = max(a,b)
arr = [ ]
i = 1
while i <= max1:
    if a % i == 0 and b % i == 0:
        arr += [ i ]
    i += 1 
max = 0
j = 1
while j < len(arr):
    if arr [ j ] > max:
        max = arr [ j ] 
    j += 1 
print(max)

