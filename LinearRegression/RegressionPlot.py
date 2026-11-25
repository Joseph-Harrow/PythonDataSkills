import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from ManualLinearRegression import gradient_descent

df = pd.read_csv("test.csv")

#Values for SciKit Learn Linear Regression Model
SkLearnX = df['x']
SkLearnX = SkLearnX.values.reshape(-1, 1)
SkLearny = df['y']

#Values for ManualLinearRegression Model
x = df['x'].tolist()
y = df['y'].tolist()

#Get slope and intercept from ManualLinearRegression, plot y values
b, m = gradient_descent(x, y, 0.00001, 100)
print(b,m)
manual_y = [m*xval + b for xval in x]

#Get linear model from SciKit and fit to data, predict y values
regr = linear_model.LinearRegression()
regr.fit(SkLearnX, SkLearny)
SkLearn_y_predict = regr.predict(SkLearnX)

#Plot data as scatter plot, and plot both Linear Regression best fit lines
plt.scatter(SkLearnX,SkLearny)
plt.plot(SkLearnX,SkLearn_y_predict,color='green')
plt.plot(x, manual_y,color='red')
plt.show()