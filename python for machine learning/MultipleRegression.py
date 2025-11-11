import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare the Data
# X has two features: "Size" (col 1) and "Bedrooms" (col 2)

X = np.array([
    [1400, 3],  # 1400 sq ft, 3 bedrooms
    [1600, 3],  # 1600 sq ft , 3 bedrooms
    [1700, 2],
    [1800, 4],
    [2000, 3],
    [2200, 4]
])

# y is the target: "Price"
y = np.array([245000, 312000, 280000, 385000, 412000, 450000])

# 2. Create and Train the Model
model = LinearRegression()
model.fit(X,y)

# 3. View the Results (The Formula's Components)
# b0 (Intercept)

intercept = model.intercept_
# b1, b2... (Coefficients)
Coefficients = model.coef_

print(f"Intercept (b0) : {intercept}")
print(f"coefficient for 'size' (b1) : {Coefficients[0]}")
print(f"coefficient for 'bedrooms' (b2) : {Coefficients[1]}")
print(f"formula for line y:")
print(f"Price = {intercept:.2f} + {Coefficients[0]:.2f}*Size + {Coefficients[1]:.2f}*Bedrooms")

# 4. Make a new prediction
# Predict the price for a 1900 sq ft, 3 bedroom house

new_house = np.array([[1900,3 ]])
prediction = model.predict(new_house)
print(f"Predicted price for a 1900 sq ft, 3-bed house: ${prediction[0]:.2f}")
