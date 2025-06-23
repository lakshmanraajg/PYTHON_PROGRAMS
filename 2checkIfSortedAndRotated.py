def fun(arr):
    
    N = len(arr)
    count = 0
    for i in range(1, 2*N):                       # 3 4 5 5 (1 2 3 4 5) 5 1 2
        if (arr[(i-1) % N] <= arr[i % N]):
            count = count + 1
        else:
            count = 1
        if count == N:                               #upto 6 == 6
            return True
    return False
    
print(fun([2,1,4,5]))
print(fun([3,4,5,5,1,2]))                         