class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def sum_list(head):
#     current = head
#     summ = 0
#     while current is not None:
#         summ += current.val
#         current = current.next
#     return summ


def sum_list(head):
    total = 0
    summ_list(head, total)
    return total


def summ_list(head, total):
    if head is None:
        return
    total += head.val
    print(total)
    summ_list(head.next, total)


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e


print(sum_list(a))
