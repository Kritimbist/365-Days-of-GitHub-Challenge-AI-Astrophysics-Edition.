import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(5.0,1.0,2000) # mean = 5.0 , SD = 1.0 and random num = 2000
y = np.random.normal( 10.0,2.0,2000) # mean = 10.0 , SD = 2.0 and random num = 2000

plt.scatter(x,y)
plt.show()
