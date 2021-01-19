class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def print(self):
        p = self
        while p is not None:
            print(p.val, end=" ")
            p = p.next
        print()


def reverse(node):
    if node.next is not None:
        p = node.next
        q = reverse(p)
        p.next = node
        node.next = None
        return q

    else:
        return node


def reverse_iter(node):
    n1 = node
    n2 = n1.next

    if n2 is None:
        return n1

    n3 = n2.next

    n1.next = None

    while n3 is not None:
        n2.next = n1

        n1 = n2
        n2 = n3
        n3 = n3.next

    n2.next = n1

    return n2


p = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
p.print()

p = reverse(p)
p.print()

p = reverse_iter(p)
p.print()
