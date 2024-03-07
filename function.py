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


