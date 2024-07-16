T = int(input())
while T > 0:
	N = int(input())
	x = (0.143*N) ** N
	floor_x = int(x)
	
	D = x - floor_x
	if D < (0.5):
		print(floor_x)
	else:
		print(floor_x+1)
	T -= 1
