T = int(input())
while T > 0:
	n,m = map(int, input().split())
	row = (m % 2) * 2 
	col = (n % 2) * m 
	print(row + col)
	T -= 1
