class Prey:

    def flee(self):
        print("This animal is fleeing")

class Predator:
    
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
#explanation: The Fish class is inheriting from both the Prey and Predator classes. This is an example of multiple inheritance. 
# The Fish class can call both the flee and hunt methods.
        