def bubble_sort(ar):
    if len(ar) <= 1:
        return ar
    if len(ar) == 2:
        if ar[0] > ar[1]:
            return [ar[1],ar[0]]
        return ar
    
    a, b = ar[0], ar[1]
    bs = ar[2:]
    res = []
    if a < b:
        res = [a] + bubble_sort([b] + bs)
    else:
        res = [b] + bubble_sort([a] + bs)
    return bubble_sort(res[:-1]) + res[-1:]

arr = [2,1,5,3]
res = bubble_sort(arr)
print(*res)