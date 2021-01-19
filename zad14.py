from basic_node import *

l = from_list([2, 4, 8, 15, 30])
print(list(l))

"""
  f
           x
      q       p
w 2 4 8 15 30
"""


def rm(first):
    wart = Node(None, first)
    x = first.val
    q = wart
    p = first.next

    while p is not None:
        if p.val % x == 0:
            x = p.val
            q.next = p
            p = p.next

        else:
            x = p.val
            q = q.next
            p = p.next

    return wart.next


l = rm(l)
print(list(l))
