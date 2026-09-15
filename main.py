# Python writing files (.text, .json, .csv)

#------------------
# .text

text_data = "I like pizza!"

file_path = "C:\\Users\\ASUS\\OneDrive\\Pictures\\Desktop\\output.txt"

#--------------
with open(file=file_path, mode="w") as file:
    file.write(text_data)
    print(f"text file '{file_path}' was created")
#--------------

#--------------
try:
    with open(file=file_path, mode="x") as file:
        file.write(text_data)
        print(f"text file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")
#--------------

try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + text_data)
        print(f"text file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")


#---------------
#---------------

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "C:\\Users\\ASUS\\OneDrive\\Pictures\\Desktop\\output.txt"

try:
    with open(file=file_path, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"text file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")

#-------------

# .json

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:\\Users\\ASUS\\OneDrive\\Pictures\\Desktop\\output.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")

#---------------
# .csv

import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "C:\\Users\\ASUS\\OneDrive\\Pictures\\Desktop\\output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")