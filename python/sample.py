a = [1, 3, 5, 7, 8]
b = [2, 3, 4, 7, 9]
i = j = 0
c = []
while i < len(a) and j < len(b):
	print(a[i],b[j])
	if a[i] == b[j]:
		c.append(a[i])
		i += 1
	else:
		j += 1 
	i += 1
print(c)
