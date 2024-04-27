#walrus operator :=
#The walrus operator := is a new operator in Python 3.8 that allows you to assign values to variables as part of an expression.
#assigns the value of the expression on the right to the variable on the left.

#happy = True
#print(happy)

print(happy := True)
#In this example, the walrus operator := is used to assign the value True to the variable happy and print it in a single line.

# food = list()
# while True:
#     food_item = input("Enter a food item: ")
#     if food_item == "quit":
#         break
#     food.append(food_item)

foods = list()
while (food_item := input("Enter a food item: ")) != "quit":
    foods.append(food_item)
