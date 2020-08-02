import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

t=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
p=np.array([0.1309, 0.2094, 0.3142, 0.3142, 0.2618, 0.4712, 0.5544, 0.6283, 0.6981, 0.6545, 0.9425, 1.0996, 1.2360, 1.2823, 1.3792, 1.4362, 1.4420, 1.5126, 1.5387, 1.7511, 1.5708, 1.4661, 1.4105, 1.4137, 1.5259, 1.6480, 1.5126, 1.5387])

def test_func(t, a, m, b):
    return a* np.arctan(m*t) + b

params, params_convariance = curve_fit(test_func, x, p)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('m:', params[1], '+-', errors[1])
print('b:', params[2], '+-', errors[2])

plt.plot(t, p , 'rx', label=r'Messwerte')
plt.plot(t, test_func(t, *params), '-', label=r'Ausgleichungskurve')
plt.ylabel(r'$\phi\,\, / \,\, \mathrm{rad}$')
plt.xlabel(r'$f \,\, / \,\, \mathrm{Hz}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-arctan.pdf')