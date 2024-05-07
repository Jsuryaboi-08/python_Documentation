#lambda function = function written in one line using lambda keyword

#lambda function can take any number of arguments but only one expression

#lambda function can be used inside another function

#lambda function can be used as an argument to another function
#lambda parameters:expression

#lambda function to add two numbers
add = lambda x, y: x + y
print(add(10, 20))

# def double(x):
#     return x * 2;
#squaring a number
square = lambda x: x * x
print(square(5))
#full name
fullname = lambda first, last: first + " " + last
print(fullname("Jeya", "Surya"))

#age check
age = lambda age: True if age >= 18 else False
print(age(19));

