arr=[7, 3, 5, 8, 4, 2, 4]
i=0
k=6
while i<len(arr)-1:
    j=i+1
    while j<len(arr):
        if arr[i]+arr[j]==k:
            a,b=arr[i],arr[j] 
            print(a,b) 
        j+=1 
    i+=1
        
        

