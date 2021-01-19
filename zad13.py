from basic_node import Node, from_list

"""
  x
q   p
7 3 5 2 1 0 4 2 6 8 4 5 4
7 5 4 6 8 5

1 2 5 4 8
4 3 2 1
"""

# l = from_list([7, 3, 5, 2, 1, 0, 4, 2, 6, 8, 4, 5, 4])
l = from_list([4])
print(list(l))


def rm(first):
    prev_val = first.val
    q = first
    p = first.next
    while p is not None:
        if p.val < prev_val:
            prev_val = p.val
            p = p.next
            q.next = p
        else:
            q = p
            p = p.next
            prev_val = q.val


rm(l)
print(list(l))
