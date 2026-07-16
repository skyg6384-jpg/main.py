# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


## Lists []

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[0])
print(fruits[0:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(dir(fruits)) # For more function
print(help(fruits))  # For all method and description
print(len(fruits))  #For length function
print("apple" in fruits)   # Using "in operator"

#fruits[0] = "pineapple"

for fruit in fruits:
    print(fruit)

#fruits.append("pineapple")
print(fruits)

#fruits.remove("apple")
print(fruits)

#fruits.insert(0, "pineapple")
print(fruits)

#fruits.sort()
print(fruits)

#fruits.reverse()
print(fruits)

#fruits.clear()
print(fruits)

print(fruits.index("banana"))

print(fruits.count("banana"))


## Sets {}

foods = {"pizza", "chicken", "apple"}
print(foods)

print(dir(foods)) # For more function
print(help(foods))  # For all method and description
print(len(foods))   # For length function
print("pineapple" in foods)

foods.add("banana")
print(foods)



## Tuples () Tuple is faster than List

Games = ("PUBG", "GTA", "FIFA")

print(Games)

print(dir(Games)) # For more function
print(help(Games))  # For all method and description
print(len(Games))   # For length function

print("Chess" in Games)

print(Games.index("GTA"))
print(Games.count("FIFA"))

for game in Games:   # In FOR LOOP
    print(game)