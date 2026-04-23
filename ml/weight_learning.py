from sklearn.linear_model import LinearRegression
import numpy as np

# sleep, work, focus
X = np.array([
    [8, 7, 9],
    [6, 5, 6],
    [7, 8, 8],
    [5, 4, 4]
])

y = np.array([92, 65, 88, 45])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[8, 6, 8]])

print("Predicted Productivity:", round(prediction[0], 2))