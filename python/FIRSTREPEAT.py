a = list(map(int, input().split()))
i = 0
e = 0
flag = 0
while i < len(a):
	j = i + 1
	while j < len(a):
		if a[i] == a[j]:
			e = a[i]
			flag = 1 
			break 
		j += 1 
		if flag == 1:
			break 
	i += 1 
if flag == 1:
	print(e)
else:
	print("No")
			
