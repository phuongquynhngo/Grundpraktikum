import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math
x1=np.array([ 0.000, 15.943, 38.263, 60.583, 79.714,100.759,122.441,145.399,165.806])
y=np.array([0.000,0.207,0.413,0.615,0.812,1.004,1.188,1.363,1.530])
x2=np.array([ 0.000, 12.754, 39.538, 66.960, 95.657,121.166,149.863,144.761,207.257])


def gerade1(x1, a1):
    return (1/(math.sqrt(8*250)))*np.sqrt(a1)*x1

params1, params1_convariance = curve_fit(gerade1, x1, y)
errors1 = np.sqrt(np.diag(params1_convariance))
print(params1)
print('a1:', params1[0], '+-', errors1[0])


def gerade2(x2, a2):
    return (1/(math.sqrt(8*420)))*np.sqrt(a2)*x2

params2, params2_convariance = curve_fit(gerade2, x2, y)
errors2 = np.sqrt(np.diag(params2_convariance))
print(params2)
print('a:', params2[0], '+-', errors2[0])




plt.plot(x1, gerade1(x1, *params1), 'r-', label=r'Ausgleichungsgerade bei $U_B$=250V')
plt.plot(x1, y, 'x',  color ='grey',  label=r'Messwerte')

plt.plot(x2, gerade2(x2, *params2), 'b-', label=r'Ausgleichungsgerade bei $U_B$=420V')
plt.plot(x2, y, 'x',  color ='grey')


plt.ylabel(r'$ \frac{D}{{L}^2+{D}^2}\,\, / \,\, (1/m)$')
plt.xlabel(r'$ B \,\, / \,\, (\mu T)$')

plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/plot.pdf')
