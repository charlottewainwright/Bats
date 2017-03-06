# Charlotte Wainwright

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

# read in the bat population CSV file

year,jday,pop = np.genfromtxt('batPop.dat',delimiter=',')

t = np.isnan(jday)
print(t)

for yr in range(1995, 2016):
    keep = np.where(year==yr)
    plt.plot(jday[keep],pop[keep])
    plt.hold(True)


#plt.plot(jday)
plt.show()

