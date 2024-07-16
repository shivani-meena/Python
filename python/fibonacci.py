N = int(input())
x = 0
y = 1 
z = 0 
while N > 0:
	print(z)
	x = y 
	y = z
	z = x + y 
	N -= 1

	
