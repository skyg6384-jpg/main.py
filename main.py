# DataFrames in Pandas

# Creating a DataFrame

import pandas as pd

data = {
    "Name": ["John", "Spongebob", "Patrick"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

print(df)
