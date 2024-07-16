a = int(input())
a.sort()
n = len(a)
i = 0
count_duplicate = 0
while i < (len(a)-1):
	if a[i] == a[i+1]:
		count_duplicate += 1
	i += 1 

