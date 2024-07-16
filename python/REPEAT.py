T = int(input())
while T > 0:
	n,k,s = map(int, input().split())
	a = 1*(k-1)
	b = 3*(k-1)
	s1 = (n**2) + a
	s2 = (n**2) + b 
	d = s2 - s1 
	i = 1
	sum = s1 - d
	while i <= (n*2):
		sum += d
		if sum == s:
			print(i)
			break 
		else:
			i += 2
	T -= 1
