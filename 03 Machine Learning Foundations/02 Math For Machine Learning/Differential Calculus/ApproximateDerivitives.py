import numpy as np
import math
#import codecademylib3
from math import sin, cos, log, pi
import matplotlib.pyplot as plt

def limit_derivative(f, x, h):
  """
  f: function to be differentiated 
  x: the point at which to differentiate f 
  h: distance between the points to be evaluated
  """
  # compute the derivative at x with limit definition
  fn_result = (f(x+h) - f(x))/h
  return fn_result

# f1(x) = sin(x)
def f1(x):
    return sin(x)

# f2(x) = x^4
def f2(x):
    return pow(x, 4)

# f3(x) = x^2*log(x)
def f3(x):
    return pow(x, 2) * log(x)

# Calculate derivatives here
x=1
h=2
r31 = limit_derivative(f3, x, h=2)
r32 = limit_derivative(f3, x, h=0.1)
r33 = limit_derivative(f3, x, h=0.00001)
r21 = limit_derivative(f2, x, h=2)
r22 = limit_derivative(f2, x, h=0.1)
r23 = limit_derivative(f2, x, h=0.00001)
r11 = limit_derivative(f1, x, h=2)
r12 = limit_derivative(f1, x, h=0.1)
r13 = limit_derivative(f1, x, h=0.00001)
print(r31, r32, r33)
print(r21, r22, r23)
print(r11, r12, r13)

# Graph the true derivative of F1
x_vals = np.linspace(1, 10, 200)
y_vals = [cos(val) for val in x_vals]
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)

# plot different approximated derivatives of f using limit definition of derivative
def plot_approx_deriv(f):
  x_vals = np.linspace(1, 10, 200)
  h_vals = [10, 1, .25, .01]

  for h in h_vals:
      derivative_values = []
      for x in x_vals:
          derivative_values.append(limit_derivative(f, x, h))
      plt.plot(x_vals, derivative_values, linestyle='--', label="h=" + str(h) )
  plt.legend()
  plt.title("Convergence to Derivative by varying h")
  plt.show()

# Plot here
plot_approx_deriv(f1)


# Calculate derivative for F2 (x^4 = 4x^3)
y_vals = [4*pow(val,3) for val in x_vals]
plt.figure(2)
plt.plot(x_vals, y_vals, label="True Derivative X^4", linewidth=4)
plot_approx_deriv(f2)

# Calculate derivative for F3 (x^2*log(x) = 2x * 1/x*log(10))
y_vals = [2*val * (1/val*math.log(10)) for val in x_vals]
plt.figure(3)
plt.plot(x_vals, y_vals, label="True Derivative X^2*log(x)", linewidth=4)
plot_approx_deriv(f3)