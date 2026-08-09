# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in


# Example 1
word = "Apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# or

words = "Banana"

letters = input("Guess a letter in the secret word: ")

if letters not in word:
    print(f"{letters} was not found")
else:
    print(f"There is a {letters}")


# Example 2

students = {"SkyGod", "Spongebob", "Sanday"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")


# or

students2 = {"SkyGod", "Spongebob", "Sanday"}

student2 = input("Enter the name of a student: ")

if student2 not in students2:
    print(f"{student2} was not found")
    print(f"{student2} is a student")
else:
    print(f"{student2} is a student")

# Example 3 in dictionary
grades = {"Sandy": "A",
          "SkyGod": "B+",
          "Spongebob": "C",
          "Sanday": "D"}

student3 = input("Enter the name of a student: ")

if student3 in grades:
    print(f"{student3}'s grade is {grades[student3]}")
else:
    print(f"{student3} was not found")

# Example 4

email = "SkyGod@gmail.com"

if "@" in email and "." in email:
    print(f"Valid email")
else:
    print(f"Invalid email")