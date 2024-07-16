a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
count = 0
while i < len(a) and j < len(b):
	if a[i] == b[j]:
		count += 1
		i += 1 
		j += 1 
	elif a[i] < b[j]:
		i += 1 
	else:
		j += 1 
print(count)
		

