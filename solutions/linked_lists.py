class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Problems:

Exercise 1--LeetCode #206 Reverse Linked List 
— reverse_list(head) → reverse in place, 

O(n) time O(1) space

"""
def reverse_list(head:ListNode)->ListNode:
    prev =  None
    curr =  head
   
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

"""
Exercise 2--LeetCode #21 Merge Two Sorted Lists —
merge_two_lists(l1, l2) → merge and return head, 
O(n+m) time O(1) space
"""

def merge_sorted_list(l1:ListNode,l2:ListNode)->ListNode:
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <l2.val:
            curr.next = l1
            l1 = l1.next

        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

"""Exercise 3--LeetCode #141 
Linked List Cycle — has_cycle(head) → fast/slow pointers,
O(n) time O(1) space

"""
def has_cycle(head:ListNode)-> bool:
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True
        
    return False

""""
Exercise 4--LeetCode #876 Middle of Linked List 
middle_node(head) → fast/slow pointers, if two middles return second, 
O(n) time O(1) space

"""

def  find_middle(head:ListNode)->ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
"""
Exercise 5--LeetCode #19 Remove Nth Node From End
remove_nth_from_end(head, n) → two pointers
O(n) time O(1) space

"""

def remove_nth_from_end(head:ListNode,n:int):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast  = dummy
    for i in range(n):
            fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next 
    return dummy.next

