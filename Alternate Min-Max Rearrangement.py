def alternate_min_max(arr):
    """
    Rearranges the array so the smallest element comes first, the largest second,
    the second-smallest third, the second-largest fourth, and so on.

    Args:
        arr (List[int]): Input list of integers.

    Returns:
        List[int]: Rearranged list in alternate min-max order.
    """

    arr.sort()  # Step 1: Sort array in ascending order
    result = []  # Resultant list to hold new arrangement

    # Step 2: Use two pointers from both ends
    left = 0
    right = len(arr) - 1

    while left <= right:
        if left == right:
            result.append(arr[left])  # Only one element left to add
        else:
            result.append(arr[left])   # Smallest remaining
            result.append(arr[right])  # Largest remaining
        left += 1
        right -= 1

    return result

# test: 

print(alternate_min_max([13, 7, 8, 3, 2, 10, 15, -1]))
# Output: [-1, 15, 2, 13, 3, 10, 7, 8]

print(alternate_min_max([-5, -12, -1, 7, 14, -7, 3, 6]))
# Output: [-12, 14, -7, 7, -5, 6, -1, 3]

print(alternate_min_max([3, 6, 9, -10, -5, -2, 0, 8]))
# Output: [-10, 9, -5, 8, -2, 6, 0, 3]
