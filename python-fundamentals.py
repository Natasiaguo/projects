# printing in teminal
print("Hello, world!")

#variable
name = "Bob" # string
print("Hello" + name + "!")

# data types
text = "apple" # string
number = 10 # integer
decimal = 10.5 # float
has_money = True/False # Boolean
coordinates = (2.5, 1.5) # tuple(list-like structure)
names = ["Agnetha", "John", "Mary"] # list
unique = {1, 2, 3, 4, 5, 6} # set(NO DUPLICATES)
user = {"Bob": 1, "James": 2} # dictionary

# convert data types
 ## wrong
number = "100"
print(10 + number)
 ## correct
number = "100"
print(10 + int(number)) # int can be replaced by any data type you want to convert it into

# F-strings
print(f"Name: {name}, Age: {age}") #instead of:
print("Name: " + name + ", Age: " + str(age))

## functions
def add(a: float, b: float) -> float:
    return a + b
print(10 + 15)
def greet(name: str, greeting: str = "Hi") -> None:
    print(f"{greeting}, {name}!")
greet("James")    

## loops
for i in range(3): # for loop: finite list of elements
    print("Hello") # print hello 3 times
names = ["Mary", "John", "Benny", "Ethan"]
for name in names:
    print(f"Hello, {name}") # greets each person in list
while True: # while loop: infinte times
    print("Hello")
i: int = 0
while i < 3:
    print(i)
    i += 1 # prints "0 1 2"

# comparison operators
a: int = 1
b: int = 2
print(a > b) # prints False
print(a >= b) # prints True
print(a < b) # prints True
print(a == b) # prints False
print(a != b) # prints True(! means not so a is not equal to b)

# if/elif/else
while True:
    user_input:str = input("You: ")

    if user_input == "hello":
        print("Bot: Hello")
    elif user_input == "How are you?": # as many elifs as you want
        print("Bot: Good, how about you?")
    else: # any other case
        print("Bot: Sorry, I did not understand that.")

# Error handling
a, b = 10, "fifteen"
try:
    print(a + b)
except TypeError as e:
    print(f"Something went wrong: {e}")
    print("Please enter a number in the form of an integer or a float...")
except Exception as e: # not recommended: absorbs all the errors
    print("Something else went wrong...")    
print("Continuing with the program...")

# imports
import math
import math as m # if you don't want to type out the entire thing
from math import sqrt, tan
print(math.sqrt(3))
print(m.sqrt(4))
print(sqrt(5))
print(tan(2))
