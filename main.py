# Random number in NumPy
import numpy as np

# For integers

#rng = np.random.default_rng(seed=1)

#print(rng.integers(low=1, high=101, size=(3, 2)))

#-------------------
# For uniform

#np.random.seed(seed=1)
#print(np.random.uniform(low=-1, high=1, size=(3, 2)))

#-------------------
# For shuffle

#rng = np.random.default_rng()

#array = np.array([1, 2, 3, 4, 5])
#rng.shuffle(array)
#print(array)

#-------------------
# For random choices

rng = np.random.default_rng()

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruits = rng.choice(fruits, size=(3, 3))
print(fruits)
