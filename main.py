# 2D Collections

fruits =     ["apple", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])
print(groceries[1][0])
print(groceries[2][0])

print()
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

print()
names = ({"sky", "apple", "banana", "coconut"},
         {"www", "jon", "space", "earth"},
         {"god", "sun", "code"})


for collection in names:
    for name in collection:
        print(name, end=" ")
    print()

print()

# Exercise 2D Keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()