n = int(input())
bin = ""
while n > 0:
    r = ( n % 2 ) 
    n = n // 2 
    bin += str( r )
s = bin + str( n )
i = -2
bin_num = " "
while i >= -len( s ):
    bin_num += s [ i ] 
    i -= 1 
print( bin_num )
   
