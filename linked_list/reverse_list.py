class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


def reverse_list(head):
    prev = None
    current = head
    
    while current:
        
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
# None <- A <- B <- C <- D
        