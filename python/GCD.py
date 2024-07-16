num1 = int(input())
num2 = int(input())
n = max(num1, num2)
i = 1
factors = []
while i < n:
	if num1 % i == 0 and num2 % i == 0:
		factors += [i]
	i += 1 
print(max(factors))


		
