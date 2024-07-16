T = int(input())
while T > 0:
	n = int(input())
	a = list(map(int, input().split()))
	i = 0
	while i < n:
		j = i + 1
		count = 0
		max_count = 0
		while j < n-1:
			if a[i] == a[j]:
				count += 1 
			j += 1 
		if count > max_count:
			max_count = count 
		i += 1 
	print(n-(max_count))
	T -= 1
