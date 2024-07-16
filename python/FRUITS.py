T = int(input())
while T > 0:
	n,m,k = map(int, input().split())
	buy_fruits = 0
	a = min(n,m)
	b = max(n,m)
	needed_fruit = abs(a-b)
	if needed_fruit <= k:
		buy_fruits = needed_fruit 
	else:
		buy_fruits = k 
	min_differnce = a + buy_fruits
	print(b - min_differnce) 
	T -= 1
