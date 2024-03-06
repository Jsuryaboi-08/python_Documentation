#multiple items store in a si9ngle variable

#basically array list in java

food = ["dosa", "idly", "vada", "poori", "chapathi", "biryani"]


print (food[4])
for x in food:
    print(x)

#negative indexing
print (food[-1])

food.append("pulav")
print(food)
food.remove("poori")
print(food)
food.pop()
print(food)
food.pop(2)#remove by index
print(food)
food.insert(2, "vada")
print(food)
food.sort()#sort in alphabetical order
print(food)
food.clear()#clear the list



