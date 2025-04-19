def plus_one(digits):
    """
    Increments the large integer represented as an array of digits by one.

    Args:
        digits (List[int]): List where each element is a digit of the number.

    Returns:
        List[int]: New list representing the incremented number.
    """

    n = len(digits)  # Get length of input array
    for i in range(n - 1, -1, -1):  # Traverse from right to left
        if digits[i] < 9:
            digits[i] += 1  # Just increment and return if no carry is needed
            return digits
        digits[i] = 0  # Set current digit to 0 if it's 9 and continue loop (carry)

    # If all digits were 9, we now have all 0's, so we insert 1 at the beginning
    return [1] + [0] * n




# test:

print(plus_one([1,2,3]))    # Output: [1,2,4]
print(plus_one([9]))        # Output: [1,0]
print(plus_one([4,3,2,1]))  # Output: [4,3,2,2]
