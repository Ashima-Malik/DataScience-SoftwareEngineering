# with dictionary

def hasCycle(self, head):
    _dict = {}
    while head:
        if head in _dict:
            return True
        else:
            _dict[head] = True
        head = head.next
    return False

# with two pointers

def hasCycle(self, head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow!= fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


