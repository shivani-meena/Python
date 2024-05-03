nums = [0,1,2,2,3,0,4,2]
val = 2

i = 0
arr = []
while i < len(nums):
    if nums[i] != val:
        arr.append(nums[i])
    i += 1 
l = len(arr)
print(l)
