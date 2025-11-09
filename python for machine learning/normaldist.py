import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0.0 , 0.7 ,150)
plt.hist(x,5) # 5 is the number of bins
plt.show()
