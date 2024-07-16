num1 = int(input())
num2 = int(input())
i = 2
a = []
b = []
while num1 > 1:
	if num1 % i == 0:
		a += [i]
		num1 = num1 // i
	else:
		i += 1 
j = 2 
while num2 > 1:
	if num2 % j == 0:
		b += [j]
		num2 = num2 // j
	else:
		j += 1 
print(a)
print(b)
