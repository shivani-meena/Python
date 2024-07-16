n = int(input())
a = list(map(int, input().split()))
N = n//2 
even = 0 
odd = 0
i = 0
while i < n:
    if a[i] % 2 == 0:
        even += 1 
    else:
        odd += 1 
    i += 1 
if n % 2 == 0:
	print(min(N,odd)+min(N,even))
else:
	print(min(N,odd)+min(N+1, even))
	
