a = list(map(int, input().split()))
i = 0
flag = 1
b = [ ]
while i < len(a):
    j = 1
    while j < max(a) // 2:
        sq = j ** 2
        if sq == a [ i ]:
            p = a [ i ]
            b.append( p )
        j += 1
    i += 1 
if len(b) != 0:
  print( b[0] )
else:
  print("No")
