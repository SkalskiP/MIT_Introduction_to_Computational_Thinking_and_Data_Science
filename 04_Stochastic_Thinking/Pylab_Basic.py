import pylab
import numpy as np

x = np.linspace(0, 20, 1000)  # 100 evenly-spaced values from 0 to 50
y = np.sin(x)

pylab.plot(x, y)
pylab.savefig('foo.png')