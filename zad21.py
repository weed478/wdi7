from basic_node import *

l = from_list([1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 1, 2, 3, 4, 5])
print(list(l))

"""
  f
a
  b
s
  e
k q p
w 1 2 3 1 2 1
"""


def rm(first):
    wart = Node(None, first)

    q = first
    p = first.next
    k = wart

    a = b = s = e = first
    max_len = 0
    current_len = 0

    while p is not None:
        if p.val > q.val:
            if current_len == 0:
                a = k
                b = p
            else:
                b = b.next

            current_len += 1

        else:
            current_len = 0

        if current_len > max_len:
            s = a
            e = b
            max_len = current_len

        k = q
        q = p
        p = p.next

    s.next = e.next

    return wart.next


l = rm(l)
print(list(l))
