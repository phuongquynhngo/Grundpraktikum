import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-1.06,-1.00,-0.95,-0.90,-0.85,-0.70,-0.65,-0.60,-0.55,-0.50,-0.45,-0.40,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05, 0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00])
y=np.array([0.000,0.000,0.000,0.000,0.000,0.032,0.032,0.045,0.045,0.045,0.055,0.063,0.063,0.071,0.077,0.089,0.089,0.100,0.105,0.110,0.118,0.126,0.141,0.148,0.155,0.161,0.167,0.179,0.184,0.190])

x1=np.array([-0.70,-0.65,-0.60,-0.55,-0.50,-0.45,-0.40,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05, 0.00])
y1=np.array([0.032,0.032,0.045,0.045,0.045,0.055,0.063,0.063,0.071,0.077,0.089,0.089,0.100,0.105,0.110])




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
plt.savefig('build/blaugrün.pdf')

