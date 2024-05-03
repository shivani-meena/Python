arr = list(map(int, input().split()))
N = len(arr)
s = int(input())
start = 0
end = N - 1

def binarySearch(start, end):
    m = (start + end) // 2
    
    if start > end:
        return -1
    else:
        if s == arr[m]:
            return m;
        elif s < arr[m]:
            return binarySearch(start, m-1)
        else:
            return binarySearch(m+1, end)
            
            
value_index = binarySearch(start, end)

if value_index == -1:
    print("Not present")
else:
    print("Value is present at index:", value_index)
    
