class animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")


class Rabbit(animal):
    def run(self):
        print("This rabbit is running")

class Fish(animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(animal):
    def fly(self):
        print("This hawk is flying")

rabbit_1 = Rabbit()
rabbit_1.eat()
rabbit_1.sleep()
rabbit_1.run()
print(rabbit_1.alive)
