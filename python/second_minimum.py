a = [7,1,2,4,6,3]
i = 0
min = a[0]
secMin = float('inf')
while i < len(a):
    if a[i] < min:
        secMin = min
        min = a[i]
    elif a[i] > min and a[i] < secMin:
        secMin = a[i]
    i += 1 
print(secMin)
