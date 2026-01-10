class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def get_node_value(head, index):
#     current = head
#     count = 0
#     while current is not None:
#         if count == index:
#             return current.val
#         count += 1
#         current = current.next
#     return None


def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 2))
