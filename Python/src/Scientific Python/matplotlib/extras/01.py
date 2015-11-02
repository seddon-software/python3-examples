import matplotlib.pyplot as plt
import numpy as np
data = np.genfromtxt('test1.dat')
months = np.arange(1,13)
monthly_mean = [x**2 for x in months]

fig, ax = plt.subplots()
ax.bar(months, monthly_mean)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly avg. temp.");
plt.show()
