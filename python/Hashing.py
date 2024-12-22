a = [1, 3, 2, 1, 5]
hash_table = [0] * 13
i = 0 
while i  < len(a):
    hash_table[a[i]] += 1 
    i += 1 
for i in range(5):
    number = int(input("Enter number"))
    print(hash_table[number])



# Character hashing if only lower case

a = "abcdacee"
hash_table = [0] * 26
i = 0 
while i  < len(a):
    hash_table[ord(a[i]) - ord('a')] += 1 
    i += 1 
for i in range(5):
    char = input("Enter number")
    print(hash_table[ord(char) - ord('a')])



# Character hashing

a = "abcdeea"
hash_table = [0] * 256
i = 0 
while i  < len(a):
    hash_table[ord(a[i])] += 1 
    i += 1 
for i in range(5):
    char = input("Enter number")
    print(hash_table[ord(char)])




# Hashing if array contain 10^9 or more size

a = [1, 2, 3, 1, 3, 2, 12]
hash_table = {}
i = 0
while i < len(a):
    if a[i] in hash_table:
        hash_table[a[i]] += 1  
    else:
        hash_table[a[i]] = 1  
    i += 1

for i in range(5):
    num = int(input("Enter a number: "))
    if num in hash_table:
        print(hash_table[num])  
    else:
        print(0) 
