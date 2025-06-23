def fun(arr):
    
    l,r = 0, len(arr) - 1
    while (l < r):
        
        m = (l + r) // 2
        
        if (arr[m] > arr[r]):
            l = m + 1
        else:
            r = m

    return arr[l]
print(fun([15,21,7,10]))