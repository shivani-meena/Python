a=[3, 5, 6, 2, 6, 4, 3, 2, 6, 3]
i=0
c=0
arr=[]
while i<len(a):
     j = 0
     c = 0
     while j < len(a):
        if a[i] == a[j]:
            c += 1
        j += 1
     if c>1:
        arr+=[a[i]]
     i += 1
print(arr)
