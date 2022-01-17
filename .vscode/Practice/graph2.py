from scipy.interpolate import make_interp_spline
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(0.001, 1)
y = -np.log(x)
model = make_interp_spline(x,y)
xs = np.linspace(0.001, 1, 2000)
ys = model(xs)
plt.plot(xs, ys)
plt.show()

