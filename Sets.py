#set is a collection of unique elements, it is unordered and unindexed

utensils = {'fork', 'spoon', 'knife'}

utensils.add('butter knife')
utensils.remove('knife')
#utensils.clear()

for x in utensils:
    print(x)
print()    


dishes = {'bowl', 'plate', 'cup', 'knife'}
#dishes.remove('fork')#error
utensils.update(dishes)#updates utensils by adding dishes
dinner_table =utensils.union() 

for x in utensils:
    print(x)

print(utensils.difference(dishes))#returns a set containing the difference between two or more sets
print(utensils.intersection(dishes))#returns a set containing the intersection of two or more sets
print(utensils.isdisjoint(dishes))#returns whether two sets have a intersection or not
print(utensils.issubset(dishes))#returns whether another set contains this set or not
print(utensils.issuperset(dishes))#returns whether this set contains another set or not
