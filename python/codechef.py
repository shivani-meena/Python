t = int(input())
while t > 0:
	n,k = map(int, input().split())
	one = k - 1
	i = 1
	s = 0
	while i <= k:
		s += i 
		i += 1 
	d = one + s 
	if d <= n:
		print("YES")
	else:
		print("NO")
	t -= 1
