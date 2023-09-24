''' task 2 '''

def decode_string(s):
    if len(s) == 0:
        return ""
        
    stack = 0
    res = ""
    last = 0
    
    for i in range(len(s)):
        if s[i] == "[":
            stack += 1
        if s[i] == "]":
            stack -= 1
            if stack == 0:
                res += get_string(s[last:i + 1])
                last = i + 1
    if last < len(s):
        res += get_string(s[last:len(s)])
        
    return res
    
        
def get_string(s):
    i = 0
    num = 0
    while s[i].isnumeric():
        num = num * 10 + int(s[i])
        i += 1
    if num == 0:
        i -= 1
        num = 1
    res = ""
    i += 1
    while i < len(s) and s[i] != "]":
        if not s[i].isnumeric():
            res += s[i]
        else:
            inside_res = get_string(s[i:len(s)])
            res += inside_res
            i += after_brackets(s[i:len(s)])
        i += 1
        
    return num * res
    
    
def after_brackets(s):
    stack = 0
    for i in range(len(s)):
        if s[i] == "[":
            stack += 1
        if s[i] == "]":
            stack -= 1
            if stack == 0:
                return i
                
    return len(s)

# tests for task 2
print(decode_string("") == "")
print(decode_string("3[a2[cd]]") == "acdcdacdcdacdcd")
print(decode_string("2[ab]3[c]db") == "ababcccdb")
print(decode_string("2[ab]3[c]") == "ababccc")
print(decode_string("2[a2[b2[c]]]") == "abccbccabccbcc")
print(decode_string("ab") == "ab")
print(decode_string("a1[b]") == "ab")
print(decode_string("a1[b]2[c]") == "abcc")
print(decode_string("a1[b2[c]]") == "abcc")
print(decode_string("a") == "a")
print(decode_string("2[a]2[b2[c2[d]2[e]]]") == "aabcddeecddeebcddeecddee")
