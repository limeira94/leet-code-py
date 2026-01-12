"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_between(head: Optional[Node], left: Optional[Node], right: Optional[Node]):
    dummy = Node(0, head)
    left_prev, cur = dummy, head
    
    for i in range(left - 1):
        left_prev, cur = cur, cur.next
    
    prev = None
    for i in range(right - left + 1):
        tmp_next = cur.next
        cur.next = prev
        prev, cur = cur, tmp_next
    
    left_prev.next.next = cur
    left_prev.next = prev
    
    return dummy.next
        
       
# 1 -> 2 -> 3 -> 4 -> 5   left = 2 right = 4
# 1 -> 4 -> 3 -> 2 -> 5