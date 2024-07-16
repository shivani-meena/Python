T = int(input())
while T > 0:
	a,b,c,d = map(int, input().split())
	p = []
	i = a 
	while i <= b:
		p.append(i)
		i += 1 
	i = c
	while i <= d:
		j = 0
		while j < len(p):
			if i != p[j]:
				p.append(i)
			j += 1 
		i += 1 
	print(p)
	T -= 1 
