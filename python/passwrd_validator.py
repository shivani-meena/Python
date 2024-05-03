a=input()
if len(a)>=8:
    i=0
    c1=0
    c2=0
    c3=0
    c4=0
    while i<len(a):
        if a[i] >="A" and a[i] <="Z":
            c1+=1
        if a[i] >="A" and a[i]<="Z":
            c2+=1 
        if a[i] >="1" and a[i] <="9":
            c3+=1 
        if a[i] =="@" or a[i] =="#" or a[i]=="$" or a[i]== "&"or a[i]=="%" or a[i]=="*":
           c4+=1 
        i+=1 
    if c1>=1 and c2>=1 and c3>=1 and c4>=1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
         
           

        

