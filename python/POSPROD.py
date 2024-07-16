T = int(input())
while T > 0:
	n = int(input())
	a = list(map(int, input().split()))
	i = 0
	pos_count = 0
	neg_count = 0
	while i < n:
		if a[i] != 0:
			if a[i] > 0:
				pos_count += 1
			else:
				neg_count += 1
		i += 1 
	a = pos_count * (pos_count-1)//2
	b = neg_count * (neg_count-1)//2
	print(a+b)
	T -= 1
