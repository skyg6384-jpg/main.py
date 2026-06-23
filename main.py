# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# String
first_name = "Sky"
food = "pizza"
email = "Sky123@fake.com"

print(first_name)
print(f"Hello {first_name}")  # f-string
print(f"You like {food}")  # using f-string
print(f"Your email is: {email}")  # using f-string


# Integers

age = 21
quantity = 3
num_of_students = 5

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float

price = 99.9
gpa = 6.74
distance = 17.8

print(f"The price is ₹{price}")
print(f"The GPA is {gpa}")
print(f"You ran {distance}Km")

# Boolean

is_student = False

print(f"Are you a student? {is_student}")
# using f-statement
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

# Example 2
for_sale = False

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

# Example 3
is_online = False

if is_online:
    print("You are online")
else:
    print("You are offline ")

