n=int(input())
b = ""
while n>0:
    r=n%2
    b=b+str(r)
    n=n//2 
bin_num = b[::-1]
print(bin_num)    
