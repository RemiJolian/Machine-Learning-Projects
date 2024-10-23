
# Let's create a basic dummy ML model in Python using `scikit-learn`:

# train_dummy_model.py
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data for training
X = np.random.rand(100, 1)
y = 2 * X.squeeze() + 0.5

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'dummy_model.joblib')

# Create a range of values for X to plot the regression line
X_range = np.linspace(0, 1, 100).reshape(-1, 1)
y_pred = model.predict(X_range)

# Plotting the data points and the regression line
plt.figure(figsize=(12, 8))
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X_range, y_pred, color='red', label='Regression Line', linewidth=2)
plt.title('Linear Regression Model')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()