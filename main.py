# Slicing

import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step]

#print(array)
#print(array[0])  # start
#print(array[0:3])  # start:end
#print(array[0:4:2])   # start:end:step
#print(array[::-1])   # row selection
#print(array[:, 0:3])   # column selection
#print(array[:, ::2])
#print(array[:, ::-1])

print(array[0:2, 0:2])   # both row & column