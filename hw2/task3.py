'''
task3
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    last = ListNode(head.val, None)
    previous = None
    current = head.next
    
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    last.next = previous
    
    return last
    
    
# # tests for task3

# def get_values_from_linked_list(head: ListNode):
#     string = ""
#     while head:
#         string += str(head.val) + " "
#         head = head.next
        
#     return string[0:len(string) - 1]
    
# # test1

# #input
# l5_in_test1 = ListNode(5, None)
# l4_in_test1 = ListNode(4, l5_in_test1)
# l3_in_test1 = ListNode(3, l4_in_test1)
# l2_in_test1 = ListNode(2, l3_in_test1)
# l1_in_test1 = ListNode(1, l2_in_test1)

# #output
# l2_out_test1 = ListNode(2, None)
# l3_out_test1 = ListNode(3, l2_out_test1)
# l4_out_test1 = ListNode(4, l3_out_test1)
# l5_out_test1 = ListNode(5, l4_out_test1)
# l1_out_test1 = ListNode(1, l5_out_test1)

# print(get_values_from_linked_list(reverse_list(l1_in_test1)) == get_values_from_linked_list(l1_out_test1))


# # test2
# #input - output
# l1_in_test2 = ListNode(5, None)

# print(get_values_from_linked_list(reverse_list(l1_in_test2)) == get_values_from_linked_list(l1_in_test2))


# # test3
# #input - output
# l2_in_test3 = ListNode(2, None)
# l1_in_test3 = ListNode(1, l2_in_test3)

# print(get_values_from_linked_list(reverse_list(l1_in_test3)) == get_values_from_linked_list(l1_in_test3))


# # test4
 #input
 l3_in_test4 = ListNode(3, None)
 l2_in_test4 = ListNode(2, l3_in_test4)
 l1_in_test4 = ListNode(1, l2_in_test4)

 #output
 l2_out_test4 = ListNode(2, None)
 l3_out_test4 = ListNode(3, l2_out_test4)
 l1_out_test4 = ListNode(1, l3_out_test4)

 print(get_values_from_linked_list(reverse_list(l1_in_test4)) == get_values_from_linked_list(l1_out_test4))
