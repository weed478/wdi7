from basic_node import *

"""
p q
w 1 4 5 7 9
  2 3 6 8
  k
  
                p q
w 1 2 3 4 5 6 7 8 9
  
  k
"""


def merge(l1, l2):
    wart = Node(None, l1)
    p = wart
    q = l1
    k = l2

    while q is not None and k is not None:
        if k.val < q.val:
            tmp = k
            k = k.next
            tmp.next = q
            p.next = tmp
            p = p.next

        else:
            p = q
            q = q.next

    if k is not None:
        p.next = k

    return wart.next


l1 = from_list([1, 4, 5, 7, 9])
l2 = from_list([2, 3, 4, 6, 7, 8])
print(list(l1))
print(list(l2))

l3 = merge(l1, l2)
print(list(l3))
