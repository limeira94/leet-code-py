class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    return_list = ListNode()
    head = return_list
    carry = 0
    while l1 or l2 or carry:
        curr_sum = 0
        if l1:
            curr_sum += l1.val
        if l2:
            curr_sum += l2.val
        curr_sum += carry
        digit = curr_sum % 10
        carry = curr_sum // 10
        