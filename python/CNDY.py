T = int(input())
while T > 0 :
	n = int(input())
	a = list(map(int, input().split()))
	i = 0
	c = []
	d = []

	while i < (n*2):
		j = i 
		co = 0
		flag = 0
		while j < (n*2):
			if a[i] == a[j]:
				co += 1 
			j += 1 
		k = 0
		while k < len(d):
			if d[k] == a[i]:
				flag = 1
			k += 1
		if flag == 0:
			d.append(a[i])
			c.append(co)
		i += 1
	f = 1 
	i = 0 
	while i < len(c):
		if c[i] > 2:
			f = 1
			break 
		else:
			f = 0
		i += 1 
	if f == 1:
		print("No")
	else:
		print("Yes")

	T -= 1
