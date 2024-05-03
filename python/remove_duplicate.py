s = input()
i = 0
st = ""
count = 0
while i < len(s):
    j = 0
    flag = 0
    while j < len(st):
        if st[j] == s[i]:
            flag = 1
        j += 1
    if flag == 0:
        st+=s[i]
    i += 1
print(st)
        
        
        
       
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
