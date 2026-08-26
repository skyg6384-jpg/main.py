# object = A "bundle" of related attributes (variables) and methods (function)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) user to design the structure and layout of an object

# -------------

from car import Car


car1 = Car("Mercedes", 1999, "blue", False)
car2 = Car("Bugatti Chiron", 2025, "black", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()  #drive
car1.stop()  #stop
car1.describe()  #describe
print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()  #drive
car2.stop()  #stop
car2.describe()  #describe