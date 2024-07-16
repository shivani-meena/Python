T = int(input())
while T > 0:
	n,m = map(int, input().split())
	num = n 
	while num <= m:
		i = 2
		c = 0
		while i <= num:
			if num % i == 0:
				c += 1 
			i += 1 
		if c == 1:
			print(num)
			print()
		num += 1
	print()
	T -= 1
