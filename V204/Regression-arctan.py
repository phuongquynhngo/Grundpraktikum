import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math

t=np.array([ 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
p=np.array([0.3016, 0.3660, 0.4098, 0.4654, 0.5386, 0.5035, 0.7854, 0.9799, 1.0996, 1.1600, 1.3165, 1.5708, 1.5111, 1.3963, 1.4923, 1.4951, 1.3443, 1.5708, 1.5708, 1.4226, 1.5359, 1.5708, 1.5259, 1.5201, 1.6250, 1.5708, 1.5450, 1.6391, 1.4544])

def test_func(t, a):
    return np.arctan(-a*2*math.pi*t)

params, params_convariance = curve_fit(test_func, t, p)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])

plt.plot(t, p , 'rx', label=r'Messwerte')
plt.plot(t, test_func(t, *params), '-', label=r'Ausgleichungskurve')
plt.ylabel(r'$\phi\,\, / \,\, \mathrm{rad}$')
plt.xlabel(r'$f \,\, / \,\, \mathrm{Hz}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-arctan.pdf')