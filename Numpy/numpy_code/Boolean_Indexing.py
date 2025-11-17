#operater indexing
import numpy as np

arr = np.array([10,15,20,25,30,35,40,45,50])
print(arr[arr>20])

# logical indexing
import numpy as np 

arr = np.array([10, 15, 20, 25, 30])

print(arr[(arr > 10) & (arr < 30)])
