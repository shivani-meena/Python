a = [1, 2, 6, 4, 5]
is_sorted = True

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Yes")
else:
    print("No")
        
