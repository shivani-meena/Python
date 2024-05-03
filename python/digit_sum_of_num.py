num = int(input())
num_str = str(num) 
l = len(num_str)
i = 0
sum = 0
while i < l:
    sum+=int(num_str[i]) 
    i += 1 
print(sum)


