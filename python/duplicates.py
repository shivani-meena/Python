a = [1,10, 3, 5, 6, 2, 6]
arr = []
i = 0
while i < len(a):
    j = 0
    c = 0
    while j < len(a):
        if a[i] == a[j]:
            c += 1
        j += 1
    if c > 1:
        arr+=[a[i]]
    i += 1
if len(arr)==0:
    print("no")
else:
    print(arr)
