a = list(map(int, input().split()))
s = 10
i = 0
flag = 0
while i < len(a):
    j = i
    sum = 0
    while j < len(a):
        sum += a[j]
        if sum == s:
            flag = 1
            break
        else:
            flag = 0
        j += 1
    if flag == 1:
        break
    i += 1
if flag == 1:
    b = i
    sub_arr = []
    while b <= j:
        sub_arr.append( a [ b ] )
        b += 1
    print(sub_arr) 
else:
    print("Not Possible")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
