## Brute force
# def partition(a,l,h):
#     pivot = a[l]
#     start = l
#     end = h
#     while (start<end):
#         while a[start] <= pivot:
#             start += 1
#         while a[end] > pivot:
#             end -= 1
#         if (start < end):
#             a[start], a[end] = a[end], a[start]
#     a[end], a[l] = a[l], a[end]
#     return end;

# def qS(a, l, h):
#     if (l<h):
#         p = partition(a,l,h)
#         qS(a, l, p-1)
#         qS(a, p+1, h)
# a = [3,2,1,5,2]
# qS(a, 0, len(a) - 1)
# print(a[len(a)-1]) 



## optimal apraoch
# a = [1, 2, 3, 4, 5, 6, 7, 9]
# i = 0
# max = 0
# sec_max = 0

# while i < len(a):
#     if a[i] > max:
#         sec_max = max  
#         max = a[i]
#     elif a[i] > sec_max: 
#         sec_max = a[i]
#     i += 1

# print("Max:", max)
# print("Second Max:", sec_max)
