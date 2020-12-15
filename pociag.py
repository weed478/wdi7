class Pociag:
    def __init__(self, val=None, next=None):
        """
        :param val: Value
        :param next: Next element
        :type next: Pociag
        """
        self.val = val
        self.next = next

    # Insertion

    def insert_after(self, val):
        """
        :param val: Element to insert
        :returns: Inserted element
        :rtype: Pociag
        """
        self.next = Pociag(val, self.next)
        return self.next

    def insert_elements_after(self, t):
        """
        :param t: Iterable of elements to insert
        :returns: Last inserted element
        :rtype: Pociag
        """
        q = self
        for i in t:
            q = q.insert_after(i)
        return q

    # Deletion

    def remove_after(self):
        """
        Remove next element

        :returns: Removed element value
        """
        if self.next is None:
            return None
        v = self.next.val
        self.next = self.next.next
        return v

    # Utility

    def __iter__(self):
        q = self
        while q is not None:
            yield q
            q = q.next

    def last(self):
        """
        Returns last element

        :returns: Last element
        :rtype: Pociag
        """
        q = self
        while q.next is not None:
            q = q.next
        return q

    def print(self):
        print(list(map(lambda i: i.val, iter(self))))


if __name__ == "__main__":
    pociag = Pociag(1)
    pociag\
        .insert_after(2)\
        .insert_after(3)\
        .insert_after(4)\
        .insert_after(5)

    pociag.insert_after(5).remove_after()

    pociag.print()


