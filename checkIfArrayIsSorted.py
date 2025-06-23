def issorted(arr):
    
    
    
    #return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return True
    return False
print(issorted([1,2,3,4,5]))
print(issorted([1,2.3,5,2,10,30,2,3,21,11,19]))