import numpy as np
x = [[3,4],[2,16]]
b=np.array([2,5,6,7])
print(b)
a = np.mat(x)
print(a.I)
b = a*a.I
print(np.linalg.inv(a))