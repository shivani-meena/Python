s = input()
# s = s.replace(" ", "")
v = "aeiouAEIOU"
c = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
i = 0
consonant = 0
vowel = 0
while i < len(s):
    j = 0
    while j < len(v):
        if s[i] == v[j]:
            vowel += 1  
        j += 1
    k = 0
    while k < len(c):
        if s[i] == c[k]:
            consonant += 1  
        k += 1 
    i += 1
print(vowel,consonant)
         

