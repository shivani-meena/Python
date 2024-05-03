def show(n):
    if n==0:
        return 1
    else:
        return show(n-1)*n
        
print(show(5))



