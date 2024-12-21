def partition(a,l,h):
    pivot = a[l]
    start = l
    end = h
    while (start<end):
        while a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if (start < end):
            a[start], a[end] = a[end], a[start]
    a[end], a[l] = a[l], a[end]
    return end;

def qS(a, l, h):
    if (l<h):
        p = partition(a,l,h)
        qS(a, l, p-1)
        qS(a, p+1, h)
a = [4, 6, 2, 5, 7, 9, 1, 3]
qS(a, 0, len(a) - 1)
print(a) 
