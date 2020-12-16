class Gar_Set2:
    def __init__(self):
        self.start = None
        self.last = None

    def __get(self, index):
        target = self.start
        while target is not None:
            if target.index == index:
                return target
            target = target.next
        return None

    def get(self, index):
        target = self.get(index)
        if target is None:
            return None
        return target.val

    def set(self, index, num):
        target = self.__get(index)
        if target is None:
            node = self.Node(index, num)
            if self.last is None:
                self.start = node
                self.last = node
            else:
                self.last.next = node
                self.last = self.last.next
        else:
            target.val = num
        return True

    def remove(self, index):
        target = self.start
        prev = None
        while target is not None:
            if target.index == index:
                if self.last == self.start:
                    self.start = None
                    self.last = None
                elif target == self.last:
                    prev.next = target.next
                    self.last = prev
                elif target == self.start:
                    self.start = target.next
                else:
                    prev.next = target.next
                # delete target
                return True

            prev = target
            target = target.next
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
        def __init__(self, index, val):
            self.val = val
            self.index = index
            self.next = None


pep = Gar_Set2()
print(pep.set(3, 6))
print(pep.set(4, 9))
print(pep.set(1, 0))
print(pep.set(91, 4))
print(pep)
print(pep.remove(5))
print(pep)
print(pep.remove(4))
print(pep)
print(pep.remove(7))
print(pep)
print(pep.remove(1))
print(pep)
