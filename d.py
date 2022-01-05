import numpy as np
a = np.arange(1, 9).reshape(4, 2)

print(np.sum(a, axis=0))
print(np.argmax(a, axis=1))
print(a[1:-1, 1:])
print(a[[1,2], :])