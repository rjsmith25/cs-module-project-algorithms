'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    newList = []
    endLen = len(nums) - k
    for i in range(0, len(nums)):
        newList.append(max(nums[i:i+k]))
        if i == endLen:
            break
    return newList


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    #      0  1   2   3  4  5  6  7
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
