# Base class
class Shape:
    def __init__(self):
        print("Shape initialized.")

    def calculate_area(self):
        pass  # Base method does nothing

# Derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Call Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        # Call Shape's constructor again from within a method (unusual but valid)
        super().__init__()
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    area = rect.calculate_area()
    print("Area of rectangle:", area)
