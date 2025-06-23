def count_rotations(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        # Case 1: already sorted subarray
        if arr[low] <= arr[high]:
            return low  # rotation count is index of minimum

        mid = (low + high) // 2
        next_idx = (mid + 1) % len(arr)
        prev_idx = (mid - 1 + len(arr)) % len(arr)

        # Case 2: mid is the smallest
        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid

        # Case 3: pivot is in left half
        if arr[mid] <= arr[high]:
            high = mid - 1
        else:
            low = mid + 1

    return 0
print(count_rotations([15, 18, 2, 3, 6, 12]))  # Output: 2
print(count_rotations([7, 9, 11, 12, 5]))      # Output: 4
print(count_rotations([1, 2, 3, 4, 5]))        # Output: 0 (not rotated)
