''' task 4 '''
# 01111111 - 127
# 10000000 - 128
# 10111111 - 191
# 11000000 - 192
# 11011111 - 223
# 11100000 - 224
# 11101111 - 239
# 11110000 - 240
# 11110111 - 247
# все, что больше 255 - остаток от деления на 256
    
def is_valid_UTF(nums):
    flag = 0
    for num in nums:
        num = num % 256
        if flag:
            if num < 128 or num > 191:
                return False
            flag -= 1
        else:
            if (num > 127 and num < 192) or (num > 247):
                return False
            else:
                if num <= 127:
                    continue
                if num >= 192 and num <= 223:
                    flag = 1
                if num >= 224 and num <= 239:
                    flag = 2
                if num >= 240 and num <= 247:
                    flag = 3
    return flag == 0
               
     
# tests for task 4
print(is_valid_UTF([197, 130, 1]) == True)
print(is_valid_UTF([197, 197, 1]) == False)
print(is_valid_UTF([1, 1]) == True)
print(is_valid_UTF([245, 130, 130, 131]) == True)
print(is_valid_UTF([245, 130, 130]) == False)
print(is_valid_UTF([245, 1, 130]) == False)
print(is_valid_UTF([197, 130, 513]) == True)
print(is_valid_UTF([255, 1, 130]) == False)
print(is_valid_UTF([]) == True)
print(is_valid_UTF([247, 197, 130, 130]) == False)
print(is_valid_UTF([247, 130]) == False)
