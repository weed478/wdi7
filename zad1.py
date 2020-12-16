class Gar_Set:
    def __init__(self):
        self.start = None

    def contains(self, num):
        target = self.start

        while target is not None:
            if target.val > num:
                break
            if target.val == num:
                return True
            target = target.next
        return False

    def add(self, num):
        target = self.start
        prev = None

        node = self.Node(num)

        if target is None:
            self.start = node
            return True

        while target is not None:
            if target.val > num:
                node.next = target
                if prev is None:
                    self.start = node
                else:
                    prev.next = node
                return True

            if target.val == num:
                return False

            prev = target
            target = target.next

        node.next = target
        prev.next = node
        return True

    def remove(self, num):
        target = self.start
        prev = None

        while target is not None:
            if target.val > num:
                break
            if target.val == num:
                if prev is None:
                    self.start = target.next
                else:
                    prev.next = target.next
                # delete target
                return True

            prev = target
            target = target.next
        return False

    def show(self):
        target = self.start
        print('[', end='')
        while target is not None:
            print(target.val, sep='', end='')
            target = target.next
            if target is not None:
                print(', ', sep='', end='')
        print(']')

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None


pep = Gar_Set()
print(pep.add(4))
print(pep.add(7))
print(pep.add(6))
pep.show()
print(pep.add(5))
pep.show()
print(pep.contains(3))
print(pep.contains(5))
print(pep.add(4))
pep.show()
print(pep.remove(5))
pep.show()
print(pep.remove(4))
pep.show()
print(pep.remove(7))
pep.show()
print(pep.remove(6))
print(pep.remove(6))
pep.show()
