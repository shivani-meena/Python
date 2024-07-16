T = int(input())
while T > 0:
	n = int(input())
	s = input()
	i = 0
	flag = 0
	while i < n:
		if s[i] == "5" or s[i] == "0":
			flag = 1 
			break
		else:
			flag = 0
		i += 1
	if flag == 1:
		print("Yes")
	else:
		print("No")
	T -= 1
