import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randn(10000)]
plt.hist(data)
plt.show()

data = [np.random.binomial(9, 0.1, 20000)]
plt.hist(data)
plt.show()

data = [np.random.uniform(50, 150, 10000)]
plt.hist(data)
plt.show()