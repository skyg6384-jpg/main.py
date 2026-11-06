# Importing Data in pandas

import pandas as pd

#file_path = Path(__file__).resolve().parent / "data.csv"

#df = pd.read_csv("data.csv")  #  Importing a CSV File: CSV stands for Comma-Separated Values.

#df = pd.read_excel("data.xlsx")  # Importing an Excel File

#--------------

# Exporting Data to CSV: We can also save a DataFrame into a CSV file.

data = {
    "Name": ["John", "Mike", "Sara"],
    "Age": [20, 25, 22]
}

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print(df)