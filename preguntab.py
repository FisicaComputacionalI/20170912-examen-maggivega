import numpy as np
import matplotlib.pylab as plt
def f(x):
   return 2* np.sin(x)+2015
x1=np.arange(0.0, 5.0, 0.1)
plt.plot(x1, f(x1), 'bo', x1, f(x1), 'k')
plt.savefig('figura2.png')
plt.show()
