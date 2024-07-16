T = int(input())
while T > 0:
	n,x = map(int, input().split())
	A = list(map(int, input().split()))
	i = 0
	s = x
	max_sum = 0
	while i < n:
		if A[i] >= 0:
			s += A[i] 
			print(s,"ss")
		else:
			if s > max_sum:
				max_sum = s 
			s = abs(s+A[i]) 
		i += 1 
	if s > max_sum:
		max_sum = s 
	print(max_sum)
	T -= 1
