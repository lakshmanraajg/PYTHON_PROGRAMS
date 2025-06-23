def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

arr = [64, 25, 12, 22, 11]

selection_sort(arr)

print("Sorted array: ",arr, end="")