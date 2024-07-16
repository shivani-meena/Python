a = list(map(int, input().split()))
a.sort()
i = 0
count = 0
l = len(a)-count
while i < (len(a)-1):
    if a[i] == a[i+1]:
	    count += 1
    i += 1 
pairs = (l*(l-1))
print(pairs//2)

