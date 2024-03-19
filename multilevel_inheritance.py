#mutlilevel inheritance = when a class is derived from a class which is also derived from another class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class DOG(Organism):#this class is derived from the Organism class
    def bark(self):
        print("This dog is barking")

print(issubclass(Animal, Organism))#this will return True
dog = DOG()
print(dog.alive)#this will return True
print(dog.bark())#this will print This dog is barking