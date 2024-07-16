T = int(input())
while T > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    count = 0
    while i <= (n-1):
        j = i + 1
        while j <= (n-1):
            bitwise_and = (arr[i] & arr[j])
            if bitwise_and == arr[i]:
                count += 1 
            j += 1 
        i += 1 
    print(count)
    T -= 1

