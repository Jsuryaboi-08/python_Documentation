#functions a block of code that only runs when it is called

def my_function(name,age):
    print("Hello from a function")
    print("My name is " + name)
    print("My age is " + str(age))

name = "surya"

my_function(name,21)

#return statement
def add(a,b):
    ADDED = a+b
    return ADDED 

print(add(2,3))

#nested function calls

num = input("enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("enter a number: ")))))

#args
#parameter that will pack all arguments into a tuple

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5)) 

#changing the tuple to list and changing the first element to 0

def Add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(Add(1,2,3,4,5))
