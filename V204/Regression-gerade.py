import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

t=np.array([0, 0.4, 1, 1.4, 2, 2.4, 3, 3.4, 4])
U_c=np.array([2.8, 2, 1, 0.7, 0.35, 0.25, 0.15, 0.1, 0.05])
U= np.log(U_c/2.8)


def test_func(t, a):
    return (-1/a)*t

params, params_convariance = curve_fit(test_func, t, U)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])

z=np.linspace(0,5)

plt.plot(t, U, 'rx', label=r'Messwerte')
plt.plot(z, test_func(z, *params), '-', label=r'Ausgleichungsgerade')
plt.ylabel(r'$ln(U_C/U_0)')
plt.xlabel(r'$t\,\, / \,\, \mathrm{ms}$')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/Regression-gerade.pdf')

