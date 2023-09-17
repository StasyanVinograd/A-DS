'''
task2
'''

def max_len_of_correct_subsequence(s) -> int:
    current_len = 0
    max_len = 0
    stack = []
    
    for i in range(len(s)):
        if s[i] == ")":
            if (len(stack) == 0 or stack[-1] != "("):
                if current_len > max_len:
                    max_len = current_len
                    current_len = 0
            else:
                stack.pop()
                current_len += 2
        else:
            stack.append(s[i])
        
    return max_len if max_len > current_len else current_len

# tests for task2
print(max_len_of_correct_subsequence("))(())((") == 4)
print(max_len_of_correct_subsequence("))") == 0)
print(max_len_of_correct_subsequence(")()") == 2)
print(max_len_of_correct_subsequence("") == 0)
print(max_len_of_correct_subsequence("()()()") == 6)
print(max_len_of_correct_subsequence("(())()") == 6)
print(max_len_of_correct_subsequence(")())()") == 2)
