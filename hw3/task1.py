''' task 1 '''

def find_peak(nums):
    left, right = 0, len(nums) - 1

    while left < right - 1:
        middle = (left + right) // 2
        if nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
            return middle
            
        if nums[middle] < nums[middle + 1]:
            left = middle + 1
        else:
            right = middle - 1
            
    return left if nums[left] >= nums[right] else right

# tests for task1
print(find_peak([1, 2, 1, 3]) == 1)
print(find_peak([1, 2, 1]) == 1)
print(find_peak([1, 2, 3, 4]) == 3)
print(find_peak([1, 2, 3, 4, 3, 4, 5, 4]) == 3)
print(find_peak([1]) == 0)
print(find_peak([2, 1]) == 0)
print(find_peak([1, 2]) == 1)
print(find_peak([1, 2, 3]) == 2)
print(find_peak([3, 2, 1]) == 0)
print(find_peak([2, 1, 3]) == 2)

