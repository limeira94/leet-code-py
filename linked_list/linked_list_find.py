class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def linked_list_find(head, target):
#     current = head
#     while current:
#         if current.val == target:
#             return True
#         current = current.next
#     return False


def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

print(linked_list_find(a, "C"))
