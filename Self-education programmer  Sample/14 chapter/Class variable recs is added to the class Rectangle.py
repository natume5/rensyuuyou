class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


recs1 = Rectangle(10, 24)
recs2 = Rectangle(20, 40)
recs3 = Rectangle(100, 200)

print(Rectangle.recs)
