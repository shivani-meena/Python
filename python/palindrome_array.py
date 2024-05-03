a = list(map(int, input().split()))
i = -1
rev = []
while i >= -len(a):
    rev.append(a[i])
    i -= 1
j = 0
flag = 0
print(rev)
while j < len(a):
  if a[j] != rev[j]:
    flag = 0
    break
  else:
    flag = 1
  j +=1
if flag == 1:
  print("Yes")
else:
  print("No")
