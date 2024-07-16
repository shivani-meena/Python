t = int(input())
while t > 0:
	c = 0
	n, x, s = map(int, input().split())
	i = 1
	while i <= s:
		a,b = map(int, input().split())
		if x == a:
			x = b 
		elif x == b:
			x = a
		i += 1 
	print(x)
	t -= 1 
