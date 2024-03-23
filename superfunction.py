#super() = superfunction
#super() is a built-in function in Python that returns the proxy object that allows you to refer parent class by 'super'.
#super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
#super() allows you to avoid using the base class explicitly, which can be more convenient and readable.
#super() is useful in multiple inheritance (where a class can inherit
# from more than one parent class) to refer to the parent class without naming them explicitly.
#super() is also useful in cases where the base class is not known ahead of time, such as in factory functions or decorators.
#super() can be used to call the __init__ method of the parent class, allowing you to initialize the parent class in the child class.
#super() can also be used to call other methods of the parent class.
#super() is used in the context of classes and inheritance.
#super() is used to call the superclass’s methods.
#super() is used to avoid using the base class explicitly.
#super() is used in multiple inheritance.
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width
class square(rectangle):
    def __init__(self, length):
        super().__init__(length, length)
class cube(square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    def volume(self):
        face_area = super().area()
        return face_area * self.length
cube = cube(3)
print(cube.surface_area())
print(cube.volume())
#explanation: In this example, we have a base class rectangle that has an area and perimeter method. We then define a square class that inherits from the rectangle class and a cube class that inherits from the square class. The cube class defines two additional methods: surface_area and volume. In the surface_area method, we use super() to call the area method of the square class, which is the superclass of the cube
# class. This allows us to calculate the surface area of the cube by multiplying the area of the square face by 6. In the volume method, we use super() to call the area method of the square class and then multiply it by the length of the cube to calculate the volume. This example demonstrates how super() can be used to call methods of the superclass in a class hierarchy.
#output:
#54
#27
#super() is a built-in function in Python that returns the proxy object that allows you to refer parent class by 'super'.