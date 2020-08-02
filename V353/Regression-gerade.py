import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

t=np.array([100, 150, 400, 600, 800, 1000, 1200, 1400, 1500, 2000, 5000, 7000, 9000, 11000, 13000])
U_c=np.array([2, 1.6, 0.75, 0.56, 0.28, 0.28, 0.28, 0.28, 0.28, 0.14, 0.07, 0.028, 0.014, 0.014, 0.014 ])
U_0=np.array([])
U= np.log(U_c / U_0)

def gerade(t, m, b):
    return m*t+b

params, params_convariance = curve_fit(gerade, t, U)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('m:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])
z = np.linspace(0,3)

plt.plot(t, U, 'rx', label=r'Messwerte')
plt.plot(z, gerade(z, *params), '-', label=r'Fit-Kurve')
plt.ylabel(r'$ln(U_C/U_0)')
plt.xlabel(r'$t\,\, / \,\, \mathrm{s}$')
plt.xscale('log')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-gerade.pdf')