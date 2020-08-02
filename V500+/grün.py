import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-0.60,-0.50,-0.45,-0.40,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05, 0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00])
y=np.array([0.000,0.045,0.063,0.089,0.118,0.161,0.210,0.257,0.293,0.361,0.406,0.447,0.524,0.583,0.648,0.693,0.735,0.812,0.883])
x1=np.array([-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05, 0.00])
y1=np.array([0.118,0.161,0.210,0.257,0.293,0.361,0.406,0.447])

def test_func(x1, a,b):
    return a*x1+b

params, params_convariance = curve_fit(test_func, x1, y1)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])


plt.plot(x, y, 'rx', label=r'Messwerte')
plt.plot(x1, test_func(x1, *params), '-', label=r'Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I}\,\, / \,\, \mathrm{\sqrt{nA}}$')
plt.xlabel(r'$U\,\, / \,\, \mathrm{V}$')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/grün.pdf')

