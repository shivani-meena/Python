T = int(input())
while T > 0:
	A1, A2, A3, A4, A5, P = map(int, input().split())
	
	work_hours = (A1 + A2 + A3 + A4 + A5) * P 
	
	if work_hours <= 120:
		print("No")
	else:
		print("Yes")

	T -= 1
