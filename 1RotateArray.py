def fun(arr,k_steps):
    
    k_steps = k_steps % len(arr)
    
    l,r = 0, len(arr) - 1
    while l < r:                                    #reversing array
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1,r-1
    
    l,r = 0,k_steps-1
    while l < r:                             #taking elements from 0 to k_steps
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1, r-1
        
    l,r = k_steps,len(arr)-1
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1, r-1
    return arr
    
print(fun([1,2,3,4,5,6,7],2))
print(fun([-1,-100,3,99],2))
    