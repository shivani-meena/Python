T = int(input())
while T > 0:
	a,b = map(int, input().split())
	i = 1 
	s1 = 0
	s2 = 0
	while True:
		if i % 2 != 0:
			s1 += i
			if (s1) > a:
				print("Bob")
				break
		else:
			s2 += i
			if (s2) > b:
				print("Limak")
				break
		i += 1 
	T -= 1
