class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"Node({self.val},{self.next})"

    def __repr__(self):
        return self.__str__()


# def print_list(head):
#     current = head
#     while current:
#         print(current.val)
#         current = current.next


def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

print_list(a)
