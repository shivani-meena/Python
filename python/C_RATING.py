T = int(input())
while T > 0:
	x,y = map(int, input().split())
	
	d = y - x
	if d % 8 == 0:
		print((d//8))
	else:
		print((d//8)+1)
		
	T -= 1
