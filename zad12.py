from basic_node import Node


class MySet:
    def __init__(self):
        self.first = None

    def __str__(self):
        return str(list() if self.first is None else list(self.first))

    def add(self, text):
        q = None
        p = self.first
        while p is not None and p.val < text:
            q = p
            p = p.next

        if p is not None and p.val == text:
            return False

        if q is None:
            self.first = Node(text, p)
        else:
            q.next = Node(text, p)

        return True

# q p
#   a b c e f g h


S = MySet()
print(S)

print(S.add("test4"))
print(S.add("test6"))
print(S.add("test4"))
print(S.add("test7"))
print(S.add("test3"))
print(S.add("test2"))
print(S.add("test1"))
print(S.add("test7"))
print(S.add("test3"))
print(S.add("test5"))

print(S)
