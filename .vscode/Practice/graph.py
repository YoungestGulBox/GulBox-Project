from scipy.interpolate import make_interp_spline
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(-5, 5)
y = 1/(1+np.exp(-x))
model = make_interp_spline(x,y)
xs = np.linspace(-5, 5, 1000)
ys = model(xs)
plt.plot(xs, ys)
plt.show()

