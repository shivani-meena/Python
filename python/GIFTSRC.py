T = int(input())
while T > 0:
	n = int(input())
	s = input()
	i = 0
	x = 0
	y = 0
	while i < n:
		if i != 0: 
			if s[i] == "L" and (s[i-1] != "L" and s[i-1] != "R"):
				x = x-1
			elif s[i] == "R" and (s[i-1] != "L" and s[i-1] != "R"):
				x = x+1
			elif s[i] == "U" and (s[i-1] != "U" and s[i-1] != "D"):
				y = y+1 
			elif s[i] == "D" and (s[i-1] != "U" and s[i-1] != "D"):
				y = y-1
		else:
			if s[i] == "L":
				x = x-1
			if s[i] == "R":
				x = x+1
			if s[i] == "U":
				y = y+1 
			if s[i] == "D":
				y = y-1
		i += 1 
	print(x,y)
	T -= 1
