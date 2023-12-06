class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def remove_dups(head):
    values = set()
    current = head
    while current and current.next:
        if current.val not in values:
            values.add(current.val)
        else:
            current.next = current.next.next
        current = current.next
    return head