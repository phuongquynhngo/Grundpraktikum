import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import semm
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

t=np.array([100, 150, 400, 600, 800, 1000, 1200, 1400, 1500, 2000, 5000, 7000, 9000, 11000, 13000])
u=np.array([2, 1.6, 0.75, 0.56, 0.28, 0.28, 0.28, 0.28, 0.28, 0.14, 0.07, 0.028, 0.014, 0.014, 0.014 ])
f_fit=np.linspace(100,15000,15000)

def test_func(t, a, m, b, c):
    return a*np.exp(-m*t+b)+c

params, params_convariance = curve_fit(test_func, t, u, p0=[1,0.0001,4,1])
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('m:', params[1], '+-', errors[1])
print('b:', params[2], '+-', errors[2])
print('c:', params[3], '+-', errors[3])

plt.plot(t, u , 'rx', label=r'Messwerte')
plt.plot(f_fit, test_func(f_fit, *params), '-', label=r'Fit-Kurve')
plt.ylabel(r'$U_C \,\, / \,\, \mathrm{V}$')
plt.xlabel(r'$f \,\, / \,\, \mathrm{Hz}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-exp.pdf')