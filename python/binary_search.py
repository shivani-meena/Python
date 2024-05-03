a = [2, 5, 7, 9, 10, 14, 17, 21, 36, 45, 60, 75]
value = int(input())

N = len(a)
start = 0
end = N - 1
flag = 0

while start <= end:
    m = (start + end) // 2
    if value == a[m]:
        flag = 1
        break
    elif value < a[m]:
        end = m - 1
    elif value > a[m]:
        start = m + 1
        
if flag == 1:
    print("Value is present at index :",m)
else:
    print("Not present")
    
