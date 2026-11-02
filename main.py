# Series

# Example 2:
# Creating a Series using a Dictionary

import pandas as pd

calories = {
    "Day 1": 2200,
    "Day 2": 2500,
    "Day 3": 1800
}

series = pd.Series(calories)

print(series)