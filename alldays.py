# Marvish Chandra

import matplotlib.pyplot as plt
from scipy import stats


allDaysARate = [0, 2.20, 3.64, 3.92, 0, 3.23, 2.60, 0]
allDaysNARate = [0, 2.20, 3.64, 3.92, 0, 3.23, 2.60, 0]

slope, intercept, r, p, std_err = stats.linregress(allDaysARate, allDaysNARate)
def allDays(x):
    return slope * x + intercept

    alldaysModel = list(map(allDays, x))

plt.scatter(allDaysARate,allDaysNARate)
plt.plot(x, allDays)
plt.show()