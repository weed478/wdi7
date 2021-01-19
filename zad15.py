from basic_node import *


def should_rm(num):
    count_1 = 0
    count_2 = 0

    while num > 0:
        num, digit = divmod(num, 3)
        if digit == 1:
            count_1 += 1
        elif digit == 2:
            count_2 += 1

    return count_1 > count_2


def from_base(text, base):
    num = 0
    for c in text:
        num *= base
        num += int(c)

    return num


"""
  f
q   p
w 1 2 3 4 5 6 7 8 9
"""


def rm(first):
    wart = Node(None, first)
    q = wart
    p = first

    while p is not None:
        if should_rm(p.val):
            p = p.next
            q.next = p

        else:
            q = p
            p = p.next

    return wart.next


l = from_list(list(map(lambda x: from_base(str(x), 3), [11122, 12332, 22, 1211211])))
print(list(l))
l = rm(l)
print(list(l))
