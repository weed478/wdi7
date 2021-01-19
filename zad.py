from basic_node import Node

l = Node(1, Node(2, Node("test", Node(4.3, Node(5)))))
print(list(l))


def last_elem(node):
    p = None
    while node is not None:
        p = node
        node = node.next

    return p


print(last_elem(l))
