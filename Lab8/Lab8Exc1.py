from abc import ABC, abstractmethod

# Step 1: Develop the Polygon class
# Polygon has one field: type
# Polygon has one constructor that initializes the field "type" from parameter
# Polygon has an abstract method 'area()' with no parameters and returns a double

class Polygon(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"{self.type}"

# Step 2: Develop the class Square
# Square is subclass of Polygon
# Square has one field: side of type double
# Square has one constructor that initializes the field side from parameter
# Square overrides the method 'area' defined in Polygon to return the area of square
# Square overrides the toString() method to return: "<type> area = <area>"

class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side
    
    def __str__(self):
        return f"{self.type} area = {self.area()}"
    
# Step 3: Develop the class Triangle
# Triangle is a subclass of Polygon
# Triangle has two double fields: height and base
# Triangle has one constructor that initializes these fields from parameters
# Triangle overrides the method 'area' defined in Polygon to return the area of a triangle
# Triangle overrides the toString() method to return: "<type> area = <area>"

class Triangle(Polygon):
    def __init__(self, height, base):
        super().__init__("Triangle")
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.height * self.base
    
    def __str__(self):
        return f"{self.type} area = {self.area()}"
    
# Step 4: Develop the class Shapes
# Shape has a field 'shapes' of type List which stores Polygon objects
# Shape has one constructor that initializes the field shapes
# Shape has a method 'loadShapes' to populate the List with the following objects:
# - 2 Square objects with sides of 5 and 10
# - 2 Triangle objects with height of 5 and base of 3, and height of 5 and base of 5
# Shape has a method 'show' that prints out information about all its Polygon objects
# Shape has the main() method that creates an instance of Shapes and invoke the method 'show'

class Shapes:
    def __init__(self):
        self.shapes = []

    def loadShapes(self):
        self.shapes.append(Square(5))
        self.shapes.append(Square(10))
        self.shapes.append(Triangle(5, 3))
        self.shapes.append(Triangle(5, 5))

    def show(self):
        for shape in self.shapes:
            print(shape)

if __name__ == "__main__":
    shapes = Shapes()
    shapes.loadShapes()
    shapes.show()