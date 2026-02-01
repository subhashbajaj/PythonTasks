import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Added outer brackets

for x in np.nditer(arr):
    print(x)