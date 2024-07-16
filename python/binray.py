num = int(input()) 
count = 0
decimal_number = 0
while num > 0:
	r = num % 10
	num = num // 10
	decimal_number += (2**count) * r
	count+= 1 
print(decimal_number)



