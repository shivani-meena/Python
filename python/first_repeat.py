a = list(map(int, input().split()))
i = 0
#count = 0
arr = []
while i < len(a):
    j = i + 1
    count = 0
    while j < len(a):
        if a[i] == a[j]:
            count += 1 
        if count > 1:
            print(a[i])
            break
        j += 1
    i += 1
print(arr)
if len(arr) != 0:
    print(arr[0])
else:
    print("No")    
                
            
            
