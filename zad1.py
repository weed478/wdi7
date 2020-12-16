class Gar_Set:
    def __init__(self):
        self.start = None

    def contains(self, num):
        target = self.start

        while target is not None and target.val < num:
            target = target.next

        if target.val == num:
            return True
        return False

    def add(self, num):
        prev = None
        target = self.start
        while target is not None and target.val < num:
            prev = target
            target = target.next

        if target is not None and target.val == num:
            return False

        node = self.Node(num)

        if prev is None:
            node.next = target
            self.start = node
            return True

        node.next = target
        prev.next = node
        return True

    def remove(self, num):
        target = self.start
        prev = None

        while target is not None and target.val < num:
            prev = target
            target = target.next

        if target is not None and target.val == num:
            if prev is None:
                self.start = target.next
            else:
                prev.next = target.next
            # delete target
            return True

        return False

    def __str__(self):
        target = self.start
        text = "["
        if target is None:
            text += "]"
            return text
        while target is not None:
            text += str(target.val) + ", "
            target = target.next
        text += "\b\b]"
        return text

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None


if __name__ == "__main__":
    pep = Gar_Set()
    print(pep.add(4))
    print(pep.add(7))
    print(pep.add(6))
    print(pep)
    print(pep.add(5))
    print(pep)
    print(pep.contains(3))
    print(pep.contains(5))
    print(pep.add(4))
    print(pep)
    print(pep.remove(5))
    print(pep)
    print(pep.remove(4))
    print(pep)
    print(pep.remove(7))
    print(pep)
    print(pep.remove(6))
    print(pep.remove(6))
    print(pep)
