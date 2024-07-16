a = list(map(int, input().split()))
a.sort()
i = 0
c = 0
b = [] 
flag = 0
while i < len(a)-1:
	if a[i] == a[i+1]:
		c += 1 
	else:
		if c != 0:
			b.append(c)  
			if (c+1) > 2:
				flag = 1
				break
		c = 0
	i += 1 
if c != 0:
	if (c+1) > 2:
		flag = 1
if flag  == 1:
	print("Yes")
else:
	print("No")
