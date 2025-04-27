import numpy as np
x = [1, 2, 3, 4, 5]
y = [4, 7, 9, 10, 11]
corrcoef = np.corrcoef(x, y)[0, 1]
print(corrcoef)