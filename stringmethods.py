name = "jeya surya"

print(len(name))
print(name.find("u"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("jeya", "surya"))
print(name.split(" "))
print(name*3)


#str.format
#more control for displaying an output

animal = "dog"
action = "bite"
print("Does your"+animal+action+"?")#Does your dog bite?
print("Does your {} {}?".format(animal, action))#Does your dog bite?
print("Does your {0} {1}?".format(animal, action))#Does your dog bite?
print("Does your {animal} {action}?".format(animal = "cat", action = "bite"))#Does your cat bite?


#.format() method takes the arguments stored in the format() method and places them in the string where the placeholders {} are

name = "jeya surya"
print("hello my name is {}".format(name))#hello my name is jeya surya
print("hello my name is {:10}".format(name))#hello my name is jeya surya
print("hello my name is {:<10}".format(name))#hello my name is jeya surya
#< left align
print("hello my name is {:>10}".format(name))#hello my name is jeya surya
#> right align
print("hello my name is {:^10}".format(name))#hello my name is jeya surya
#^ center align

#number formatting
pi = 3.14159265359
print("pi is equal to {}".format(pi))#pi is equal to 3.14159265359
print("pi is equal to {:.2f}".format(pi))#pi is equal to 3.14
print("pi is equal to {:.4f}".format(pi))#pi is equal to 3.1416
print("pi is equal to {:b}".format(pi))#pi is equal to 11
print("pi is equal to {:o}".format(pi))#pi is equal to 3 octal
print("pi is equal to {:x}".format(pi))#pi is equal to 3.243f6a8885a3 hexadecimal
print("pi is equal to {:e}".format(pi))#pi is equal to 3.141593e+00 scientific notation