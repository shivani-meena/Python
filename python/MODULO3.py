T = int(input())
while T > 0:
	a, b = map(int, input().split())
	dif = abs(a-b) 
	if a % 3 == 0 or b % 3 == 0:
		print(0) 
	elif dif % 3 == 0:
		print(1) 
	else:
		print(2)
	T -= 1
