import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

t=np.array([50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
u=np.array([2.6, 2.6, 2.6, 2.5, 2.48, 2.42, 1.92, 1.5, 1.2, 1, 0.85, 0.72, 0.65, 0.58, 0.5, 0.256, 0.17, 0.138, 0.11, 0.09, 0.078, 0.069, 0.059, 0.055, 0.05, 0.046, 0.042, 0.0396, 0.032])

def test_func( t, a, m, b):
    return a*(t**m)+b

params, params_convariance = curve_fit(test_func, t, u)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('m:', params[1], '+-', errors[1])
print('b:', params[2], '+-', errors[2])

plt.plot(t, u , 'rx', label=r'Messwerte')
plt.plot(t, test_func(t, *params), '-', label=r'Fit-Kurve')
plt.ylabel(r'$U_C \,\, / \,\, \mathrm{V}$')
plt.xlabel(r'$f \,\, / \,\, \mathrm{Hz}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-exp.pdf')



