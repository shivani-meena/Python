T = int(input())
while T > 0:
	s = input()
	n = len(s) 
	i = 0
	a = 0
	while i < n:
		if s[i] == "a":
			a += 1 
		i += 1 
	b = n - a
	print(min(a,b))
	T -= 1
