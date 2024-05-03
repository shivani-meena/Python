'''
    Instructions:
        1. Write your code below "WRITE YOUR LOGIC HERE" after removing the pass statement
        2. Take input from terminal
           e.g.
           s1: pale
           s2: ealp
        3. Return True if strings are almost equal, else return False
'''

def areAlmostEqual(s1: str, s2: str) -> bool:
    j = 0
    k = list(s2)
    c = 0
    d =[]
    while j < len(s1):
        if s1[j] in s2:
            if s1[j] != s2[j]:
                d.append(j)
                c+=1
        j += 1

    if c == 2:    
        k[d[0]],k[d[1]] = k[d[1]],k[d[0]]
        new_string = "".join(k)  
        if s1 == new_string:
            return True
    elif c == 0:
        return True
    else:
        return False    
        
# DO NOT CHANGE ANYTHING BELOW THIS LINE
if __name__ == '__main__':
    s1 = input("s1: ")
    s2 = input("s2: ")
    if areAlmostEqual(s1, s2):
        print("true")
    else:
        print("false")