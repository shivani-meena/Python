n = int(input()) 
count = 0
i = 1
while i < n:
    if n % i == 0:
        count += 1 
    i += 1 
if count > 1:
    print("No")
else:
    print("Yes")
