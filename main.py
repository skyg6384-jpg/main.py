# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]   # class 'int'

for number in reversed(numbers):
    print(number)
print()


items = ("apple", "banana", "cherry")   # class 'str'

for item in reversed(items):
    print(item, end=" ")
print()
print()


# ---------
# 'set' object is not reversible
# ---------

name = "Sky God"

for name in reversed(name):
    print(name, end="")
print()
print()


my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")