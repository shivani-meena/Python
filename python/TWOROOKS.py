T = int(input())
while T > 0:
	x1,y1,x2,y2 = map(int, input().split())
	if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2):
		print("Yes")
	else:
		print("No")
	T -= 1
