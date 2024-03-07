#keyword arguments = kwargs
#arguments preceeded by an identifier in the function call
#when we use keyword arguments in a function call, the caller identifies the arguments by the parameter name
#this allows us to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters
#syntax: def function(a,b,c):

def hello(first_name,last_name):
    print("Hello " + first_name + " " + last_name)


hello(last_name = "surya", first_name = "jeya")#Hello jeya surya
hello("surya", "jeya")#Hello surya jeya
    