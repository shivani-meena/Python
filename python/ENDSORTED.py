T = int(input())
while T > 0:
	n = int(input())
	a = list(map(int, input().split()))
	
	i = 0 
	index_one = 0 
	index_n = 0 
	
	while i < n:
		if a[i] == 1:
			index_one = i 
		if a[i] == n:
			index_n = i 
		i += 1 
		
	j = 0
	count1 = 0
	count2 = 0
	while j < n:
		if j < index_one:
			count1 += 1
		if j > index_n:
			count2 += 1 
		j += 1 
	s = count1 + count2
	if index_one > index_n:
		print(s-1)
	else:
		print(s)
		
	T -= 1
