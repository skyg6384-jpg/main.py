# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "SKY GOD"
age = 21
gpa = 6.7
is_student = True

print(type(name))   # class 'str'
print(type(age))    # class 'int'
print(type(gpa))    # class 'float'
print(type(is_student))  # class 'bool'

# Examples :

#float ---> int

gpa = int(gpa)

print(gpa)

#int ---> float

age = float(age)

print(age)

# int ---> str

age = str(age)

print(type(age))

age += "1"

print(age)

#str ---> bool

name = bool(name)

print(name)