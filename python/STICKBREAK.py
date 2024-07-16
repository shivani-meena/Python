T = int(input())
while T > 0:
	l, k = map(int, input().split())
	if l % k == 0:
		print(0)
	else:
		print(1)
	T -= 1
