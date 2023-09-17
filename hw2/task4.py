'''
task4
'''

def time_for_buy(ticket, k):
    buyer = ticket[k]
    time = 0
    for i in range(len(ticket)):
        if ticket[i] < buyer:
            time += ticket[i]
            
        if ticket[i] == buyer and i <= k:
            time += ticket[i]
            
        if ticket[i] > buyer:
            time += buyer
            if i > k:
                time -= 1
            
    return time
    
# tests for task4
print(time_for_buy([2, 3, 2], 2) == 6)
print(time_for_buy([1, 3, 2, 1], 2) == 6)
print(time_for_buy([1, 3, 2, 1, 4], 2) == 7)
print(time_for_buy([1, 2, 3], 2) == 6)
print(time_for_buy([1, 2, 3], 2) == 6)
print(time_for_buy([1, 3, 5], 0) == 1)
print(time_for_buy([5, 3, 1], 0) == 9)
print(time_for_buy([1, 3, 7, 5], 1) == 8)
