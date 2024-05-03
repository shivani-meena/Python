s = input().lower()
n = input().lower()
i = 0
count = 0
while i < len(s):
    if s[i] == n:
        count += 1
    i += 1 
if count > 1:
    print(count)
else:
    print("No")
