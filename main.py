# Creating a Series with Custom Index

import pandas as pd

data = [85, 90, 78]

s = pd.Series(data, index=["Math", "Science", "English"])

print(s)