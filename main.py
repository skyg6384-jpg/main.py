# Python reading files (.text, .json, .csv)

import json
import csv

file_path = "C:/Users/ASUS/OneDrive/Pictures/Desktop/output.csv"  # (txt, json, csv)

try:
    with open(file_path, "r") as file:
        #content = file.read()  #txt
        #content = json.load(file)   #json
        content = csv.reader(file)
        for line in content:
            print(line)  #csv
        #print(content)  #txt, json only using
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read the file")