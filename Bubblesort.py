def bubbleSort(arr):
    n = len(arr)
    flag = True
    
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1],arr[i] = arr[i],arr[i-1]
        

arr = [5,6,1,3]
bubbleSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i], end = " ")