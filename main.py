# While loop = execute some code WHILE some condition remains true


# While loop

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

# Infinite loop ♾️

ok = input("Enter you are ok: ")

while ok == "":
    print("You are ok")

print(f"Hello {ok}")

# Exercise 1

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")