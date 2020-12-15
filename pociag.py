class Pociag:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def insert_after(self, val):
        self.next = Pociag(val, self.next)
        return self.next

    def remove_after(self):
        v = self.next.val
        self.next = self.next.next
        return v

    def __iter__(self):
        q = self
        while q is not None:
            yield q
            q = q.next


if __name__ == "__main__":
    pociag = Pociag(1)
    q = pociag

    q = q.insert_after(2)
    q = q.insert_after(3)
    q = q.insert_after(4)
    q.insert_after(5)

    q = pociag.insert_after(5)
    q.remove_after()

    for q in pociag:
        print(q.val)


