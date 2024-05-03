n = int(input()) 
i = 0
reverse_num = ""
while n > 0:
    a = n % 10
    n = n // 10 
    reverse_num += str(a) 
print(reverse_num)






class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        reverse_num = 0
        while n > 0:
            a = n % 10
            reverse_num = (reverse_num*10) + a 
            n = n // 10 
        if x == reverse_num:
            return True
        else:
            return False 
