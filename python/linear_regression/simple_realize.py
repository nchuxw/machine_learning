#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plot

# x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# y = np.array([1.0, 3.0, 2.0, 3.0, 5.0])
# plot.axis([0, 6, 0, 6])
# plot.scatter(x, y)
# plot.show()

# x_mean = np.mean(x)
# y_mean = np.mean(y)
# num = 0.0
# div = 0.0
# for x_i, y_i in zip(x, y):
#     num += (x_i - x_mean) * (y_i - y_mean)
#     div += (x_i - x_mean) ** 2
# a = num /div
# b = y_mean - a * x_mean
# y_hat = a * x + b

# print("a=", a, "b=", b)
# plot.axis([0, 6, 0, 6])
# plot.scatter(x, y)
# plot.plot(x, y_hat, color="r")
# plot.show()


import simple_linear_regression
m = 100
X_train = np.random.random(size=m)
Y_train = X_train * 2.0 + 3.0 + np.random.normal(size=m)
slr = simple_linear_regression.SimpleLinearRegression()
slr.fit(X_train, Y_train)
a = slr.a_
b = slr.b_
Y_hat = a * X_train + b

print("a=", a, "b=", b)
plot.scatter(X_train, Y_train)
plot.plot(X_train, Y_hat, color="r")
plot.show()