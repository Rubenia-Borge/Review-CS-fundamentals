# -*- coding: utf-8 -*-
"""day_11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zmHgQwut9Tih8_5fsoEe0ZvmiUW20Y9P

Linear Regression with scikit-learn

```
# Steps:
1) Import the Python libraries needed
2) Load the data that will be used in the Regression and make the required data transformations for the model to run
3) Create a Regression model
4) Fit the Regression model with the data previously loaded
5) Get the results of fitting the model
6) Verify the results of the model fitting
7) Apply the model to make new predictions
```
"""

# Import the Python libraries needed
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data that will be used in the Regression and make the required data transformations for the model to run
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# Create a Regression model
# Fit the Regression model with the data previously loaded

model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)

# Get the results of fitting the model
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

# Verify the results of the model fitting
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# Apply the model to make new predictions
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')



import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define Sequential model with 3 layers
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)
# Call model on a test input
x = tf.ones((3, 3))
y = model(x)

# Create 3 layers
layer1 = layers.Dense(2, activation="relu", name="layer1")
layer2 = layers.Dense(3, activation="relu", name="layer2")
layer3 = layers.Dense(4, name="layer3")

# Call layers on a test input
x = tf.ones((3, 3))
y = layer3(layer2(layer1(x)))

model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)

model.layers