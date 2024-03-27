#duck typing:concept where the class of the class is less important than the methods it defines.
#"if it looks like a duck and quacks like a duck, it must be a duck"

class Duck:
    def walk(self):
        print("Duck is walking")
    def talk(self):
        print("Duck is qwacking")

class Chicken:
    def walk(self):
        print("Chicken is walking")
    def talk(self):
        print("Chicken is clucking")

class Person:
    def catch(self,animal):
        animal.walk()
        animal.talk()
        print("Caught the animal")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
#explanation: the catch method of the Person class takes an object as an argument. The object can be of any class as long as it has the walk and talk methods.
#The catch method calls the walk and talk methods of the object and prints "Caught the animal" at the end.
#This is an example of duck typing because the class of the object is not important as long as it has the required methods.
#In this case, both the Duck and Chicken classes have the walk and talk methods, so they can be passed to the catch method of the Person class.
#This is in contrast to static typing, where the type of the object is important when passing it as an argument to a method.
#In static typing, the object must be of a specific class or a subclass of that class to be passed as an argument.
#Duck typing allows for more flexibility and reusability of code, as any object with the required methods can be passed to the method.
#This makes the code more generic and easier to maintain, as new classes can be added without changing the existing code.
