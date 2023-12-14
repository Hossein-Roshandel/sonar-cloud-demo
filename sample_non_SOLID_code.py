# This is a sample code to demonstrate the violation of SOLID principles.
# Also some passwords are in the file. Please do not use them.

username = "admin"
password = "admin"

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def get_area(self):
        return self.length * self.length
    
    def get_perimeter(self):
        return 4 * self.length

if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print("Area of rectangle: ", rectangle.get_area())
    print("Perimeter of rectangle: ", rectangle.get_perimeter())
    if password == "admin":
        print("Password is correct")
    square = Square(5)
    print("Area of square: ", square.get_area())
    print("Perimeter of square: ", square.get_perimeter())
