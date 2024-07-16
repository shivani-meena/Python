T = int(input())
while T > 0:
	N, K = map(int, input().split())
	A = list(map(int, input().split()))
	i = 0
	array_sum = 0
	while i < N:
		array_sum += A[i]
		i += 1 
	if K == 1:
		if array_sum % 2 == 0:
			print("odd")
		else:
			print("even")
	else:
		print("even")
	T -= 1
