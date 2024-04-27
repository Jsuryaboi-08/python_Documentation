#higher order functions
# A higher-order function is a function that takes another function as an argument or returns a function as a result.
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
# In this example, the loud and quiet functions are defined, which convert text to uppercase and lowercase, respectively.
# The hello function takes another function as an argument and calls it with the text "Hello".
# The loud function is passed to the hello function, resulting in the text "HELLO" being printed.
hello(quiet)
# In this example, the quiet function is passed to the hello function, resulting in the text "hello" being printed.         
# This demonstrates how higher-order functions can be used to pass functions as arguments to other functions.
# A higher-order function can also return a function as a result.

def divisor(n):
    def dividend(x):
        return x / n
    return  dividend

divide = divisor(2)
print(divide(10))
# In this example, the divisor function takes a number n as an argument and returns another function called dividend.
# The dividend function takes a number x as an argument and returns the result of dividing x by n.
# The divisor function is called with the argument 2, resulting in the dividend function being returned.
