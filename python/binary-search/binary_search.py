def binary_search(nums, n, i=0):
    if len(nums) == 0:
        raise ValueError("not found")
    mid = len(nums) // 2
    if n == nums[mid]:
        return nums.index(n) + i
    elif n < nums[mid]:
        return binary_search(nums[:mid], n, i)
    else:
        return binary_search(nums[mid + 1:], n, len(nums[:mid]) + i + 1)
