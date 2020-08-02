import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([4.688,5.180,5.495,6.103,6.884])
y=np.array([-0.231,-0.522,-0.470,-0.940,-1.113])


def test_func(x, a,b):
    return a*x+b

params, params_convariance = curve_fit(test_func, x, y)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])


plt.plot(x, y, 'rx', label=r'Messwerte')
plt.plot(x, test_func(x, *params), '-', label=r'Ausgleichsgerade')
plt.ylabel(r'$ U_g \,\, / \,\, \mathrm{V}$')
plt.xlabel(r'$ \nu \,\, / \,\, \mathrm{ 10^{14} \, Hz}$')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/gegenspannung.pdf')

