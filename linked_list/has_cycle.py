"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def has_cycle(head: Optional[ListNode]) -> bool:
#     if head is None:
#         return False

#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False

# Time O(n) and Space O(n)
def has_cycle(head: Optional[ListNode]):
    seen = set()
    current = head
    
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False
        
def test_1():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node4.next = node2

    assert has_cycle(node1) is True
