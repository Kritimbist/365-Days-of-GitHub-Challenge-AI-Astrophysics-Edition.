import numpy as np
array_2d = np.array([[1,2,3],[4,5,6]])
scalar = 10
result = array_2d + scalar
print(result)

import numpy as np

arr = np.array([1,2,3,4])
res = arr + 1
print(res)

import numpy as np
a1 =np.array([2,3,6])
a2 = np.array([[1,3,5],[7,8,9]])
res = a1+a2
print(res)

import numpy as np
ages = np.array([12,24,56,35,60,72,4])
age_group =np.array(["Adult","Minor"])
res = np.where(ages>18, age_group[0], age_group[1])
print(res)

import numpy as np
matrix =np.array([[1,2],[3,4]])
vector = np.array([10,20])
res = matrix * vector
print(res)
