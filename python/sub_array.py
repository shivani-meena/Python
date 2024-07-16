a = list(map(int, input().split()))
i = 0
while i < len(a):
	j = i 
	b = []
	while j < len(a):
		b.append(a[j])
		print(*b)
		j += 1
	i += 1 

	
