from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import time
start = time.time()
x = np.arange(20)
y = x ** 2

plt.plot(x,y)
plt.show()
end = time.time()

print ("done")