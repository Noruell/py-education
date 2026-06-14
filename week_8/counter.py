# counter
class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1
        self.number = Counter.total

c1 = Counter()
c2 = Counter()
print(Counter.total)  # 2
print(c1.number)      # 1
print(c2.number)      # 2

# rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def is_square(self):
        return True if self.width == self.height else False

r = Rectangle(4, 5)
print(r.area())        # 20
print(r.perimeter())   # 18
print(r.is_square())   # False