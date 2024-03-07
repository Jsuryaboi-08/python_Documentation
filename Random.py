import random

x = random.randint(1, 6)
print (x)
#random.randint(a,b) returns a random number between a and b including a and b

y = random.random()#random number between 0 and 1
print (y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print (z)
#random.choice(sequence) returns a random element from the non-empty sequence

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)
print (cards)
#random.shuffle(sequence) shuffles the sequence in place
#sequence can be a list, a tuple or a string
#tuple
Tup = (1,2,3,4,5,6,7,8,9,10,"J","Q","K","A")
#string
string = "12345678910JQKA"
#list
List = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
