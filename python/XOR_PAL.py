T = int(input())
while T > 0:
    N = int(input())
    A = input()
    j = N-1
    i = 0
    count_one = 0
    
    while i < (N//2):
        if A[i] != A[j]:
            count_one += 1
        j -= 1
        i += 1 
    if count_one % 2 == 0:
        print(count_one//2)
    else:
        print((count_one//2)+1)
    T -= 1
