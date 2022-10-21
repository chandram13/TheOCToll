# Marvish Chandra

import matplotlib.pyplot as plt
from scipy import stats

mfnARate = [6.89, 8.24, 9.00, 8.24, 6.89, 6.60]
mfsnNARate = [9.00, 9.00, 9.00, 9.00, 9.00, 9.00]

slope, intercept, r, p, std_err = stats.linregress(mfnARate, mfsnNARate)

def catalinaNorthbound(x):
    return slope * x + intercept

northboundModel = list(map(catalinaNorthbound, x))

plt.scatter(mfnARate,mfsnNARate)
plt.plot(x, northboundModel)
plt.show()
