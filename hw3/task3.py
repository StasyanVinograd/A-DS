''' task 3 '''

def find_min(nums):
    if len(nums) == 0:
        return -1
        
    left, right = 0, len(nums) - 1

    while left < right:

        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    
    return nums[left]
    
# tests for task 3
print(find_min([2, 2, 2, 0, 1]) == 0)
print(find_min([0, 1, 2, 3, 4]) == 0)
print(find_min([5, 6, 6, 0, 0, 1, 2, 3, 4]) == 0)
print(find_min([1]) == 1)
print(find_min([]) == -1)
print(find_min([1, 2, 2, 3]) == 1)
