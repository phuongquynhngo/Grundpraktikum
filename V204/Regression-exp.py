import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math

t=np.array([50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
u=np.array([0.9286, 0.9286, 0.9286, 0.8929, 0.8857, 0.8643, 0.6857, 0.5357, 0.4286, 0.3571, 0.3036, 0.2571, 0.2321, 0.2071, 0.1786, 0.0914, 0.0607, 0.0493, 0.0393, 0.0321, 0.0279, 0.0246, 0.0211, 0.0196, 0.0179, 0.0164, 0.0150, 0.0141, 0.0114])


def test_func( t, a):
    return 1/((1+((a**2)*(2*math.pi*t)**2))**(1/2))

params, params_convariance = curve_fit(test_func, t, u)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])


plt.plot(t, u , 'rx', label=r'Messwerte')
plt.plot(t, test_func(t, *params), '-', label=r'Ausgleichungskurve')
plt.ylabel(r'$A_C/U_0')
plt.xlabel(r'$f \,\, / \,\, \mathrm{Hz}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-exp.pdf')



