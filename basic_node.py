class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return repr(self.val)

    def __iter__(self):
        p = self
        while p is not None:
            yield p
            p = p.next


def from_list(t):
    l = Node(t[0])
    p = l
    for i in t[1:]:
        p.next = Node(i)
        p = p.next

    return l
