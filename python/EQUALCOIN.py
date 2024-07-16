T = int(input())
while T > 0:
	x,y = map(int, input().split())
	if x % 2 == 0 and x != 0:
	    print("YES")
	elif y % 2 == 0 and x == 0:
		print("YES")
	else:
		print("NO")
	T -= 1
	
