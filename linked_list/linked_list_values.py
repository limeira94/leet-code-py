class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def linked_list_values(head):
#     current = head
#     values = []
#     while current:
#         values.append(current.val)
#         current = current.next
#     return values


# def linked_list_values(head):
#     values = []
#     if head is None:
#         return
#     values.append(head.val)
#     linked_list_values(head.next)
#     return values


def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values


def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)


# A -> B -> C -> D
# [A, B, C, D]

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

print(linked_list_values(a))
