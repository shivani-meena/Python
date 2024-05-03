a = int(input())
n = str(a) 
sum = 0
i = 0
while i < len(n):
    sum += int(n[i])**len(n) 
    i += 1 
if a == sum:
    print("Yes")
else:
    print("No")
