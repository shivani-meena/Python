num = int(input())
i = 1
while i*i <= num:
    if num % i == 0:
        if i != (num//i):
            print(i, num//i, end = " ")
        else:
            print(i)
    i += 1 
