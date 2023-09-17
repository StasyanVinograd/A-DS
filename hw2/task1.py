'''
task 1
'''

def find_sequence_sum(a, m) -> [int]:
    res = []
    current_sum = 0
    
    for i in range(m):
        current_sum += a[i]
        
    res.append(current_sum)
    for i in range(m, len(a)):
        current_sum -= a[i - m]
        current_sum += a[i]
        res.append(current_sum)
        
    return res


# tests for task1
print(find_sequence_sum([1, 6, 78, 12], 3) == [85, 96])
print(find_sequence_sum([1, 2, 3, 4, 5, 6, 7], 3) == [6, 9, 12, 15, 18])
print(find_sequence_sum([1, 2, 3], 3) == [6])
print(find_sequence_sum([1, 2, 3], 1) == [1, 2, 3])
print(find_sequence_sum([-50, 2, 0, 78], 2) == [-48, 2, 78])
print(find_sequence_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [3, 5, 7, 9, 11, 13, 15, 17, 19])
