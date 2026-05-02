import math
class Circle:
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius
    def get_area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
    def get_perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
my_circle = Circle(5)
print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.get_area():.2f}")
print(f"Perimeter: {my_circle.get_perimeter():.2f}")