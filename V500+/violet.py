import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-1.12,-1.11,-1.10,-1.08,-1.05,-1.00,-0.95,-0.90,-0.85,-0.80,-0.75,-0.70,-0.60,-0.50,-0.40,-0.30,-0.20,-0.10,0.00,0.10,0.20,0.30,0.40,0.60,0.80,1.00])
y=np.array([0.000,0.032,0.045,0.055,0.063,0.089,0.118,0.148,0.173,0.205,0.237,0.276,0.354,0.436,0.515,0.583,0.663,0.721,0.787,0.849,0.906,0.959,1.000,1.095,1.183,1.245])
x1=np.array([-1.00,-0.95,-0.90,-0.85,-0.80,-0.75,-0.70,-0.60,-0.50,-0.40,-0.30,-0.20,-0.10,0.00,0.10,0.20,0.3])
y1=np.array([0.089,0.118,0.148,0.173,0.205,0.237,0.276,0.354,0.436,0.515,0.583,0.663,0.721,0.787,0.849,0.906,0.959])

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
plt.savefig('build/violet.pdf')

