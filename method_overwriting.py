class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def speak(self):
        print("Dog Barking")

dog = Dog()
#method overwriting
dog.speak()
#explanation: The speak method in the Dog class overwrites the speak method in the Animal class.
# This is an example of method overwriting.