# Python file detection

import os

file_path = "C:/Users/ASUS/OneDrive/Pictures/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists")

    if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")