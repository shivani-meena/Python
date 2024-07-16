T = int(input())
while T > 0:
	n = int(input())
	a = list(map(int, input().split()))
	i = 0
	pos = 0
	neg = 0
	c1 = 0
	c2 = 0
	while i < n:
		if a[i] > 0:
			pos += a[i]
			c1 += 1
		else:
			neg += a[i]
			c2 += 1
		i += 1 
	if pos == 0 or neg == 0:
		print(c1 + c2, c1 + c2)
	elif pos > -neg:
		print(c1, c2)
	elif pos == -neg:
		print(c1, c2)
	else:
		print(c2, c1)
	T -= 1
