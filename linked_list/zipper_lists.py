class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_lists(head_1, head_2):
    tail = head_1
    cur1 = head_1.next
    cur2 = head_2
    count = 0

    while cur1 and cur2:
        if count % 2 == 0:
            tail.next = cur2
            cur2 = cur2.next
        else:
            tail.next = cur1
            cur1 = cur1.next
        tail = tail.next
        count += 1

    if cur1:
        tail.next = cur1
    if cur2:
        tail.next = cur2
    return head_1


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)