T = int(input())
while T > 0:
	N = int(input())
	B = list(map(int, input().split()))
	i = 0
	count_one = 0
	while i < N:
		if B[i] == 1:
			count_one += 1 
		i += 1 
	if count_one % 2 == 0:
		print("YES")
	else:
		print("NO")
	T -= 1
