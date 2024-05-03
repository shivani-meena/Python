def fibonacci(a):
    if a == 2:
        return 1
    elif a == 1:
        return 0
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

for i in range(10):
    print(fibonacci(i))
