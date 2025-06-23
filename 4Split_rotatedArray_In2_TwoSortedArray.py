def find_pivot(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            # Pivot must be to the right
            low = mid + 1
        else:
            # Pivot could be mid or to the left
            high = mid
    return low  # Index of the smallest element

def split_rotated_array(arr):
    if not arr:
        return [], []

    pivot = find_pivot(arr)

    # Split into two sorted arrays
    return arr[pivot:], arr[:pivot]

# Test
arr = [4, 5, 6, 7, 0, 1, 2]
sorted1, sorted2 = split_rotated_array(arr)
print("First Sorted Part:", sorted1)
print("Second Sorted Part:", sorted2)
