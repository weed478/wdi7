from pociag import Pociag

p = Pociag(1)
p.insert_elements_after([2, 3, 4, 5])
p.print()

p.last().insert_after(0)
p.print()
