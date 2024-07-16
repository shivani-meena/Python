a = input()
b = input() 
c = list(a)
d = list(b)
i = 0
count = 0
while i < len(a):
	if a[i] != b[i]:
		count += 1
		
	i += 1
if count == 2 or count == 0:
	print("yes")
else:
	print("no")

				
