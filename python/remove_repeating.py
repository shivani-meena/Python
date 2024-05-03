n = input()
str = ""
i = 0
while i < len(n):
    j = 0
    flag = 0
    while j < len(str):
        if str[j] == n[i]:
            flag = 1 
        j += 1
    if flag == 0:
        str+=n[i] 
    i += 1
print(str)
                
