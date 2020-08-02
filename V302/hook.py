import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x = np.array([0.06,0.12,0.18,0.24,0.30,0.32,0.36,0.42,0.48,0.54])
F = np.array([0.18,0.36,0.53,0.71,0.89, 0.95, 1.07, 1.25, 1.44,1.61])

def test_func(x, m, b):
    return m * x + b

params, params_covariance = curve_fit(test_func,x,F)
errors = np.sqrt(np.diag(params_covariance))
print(params)
print('m:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

line1 = np.linspace(0,0.54)

plt.plot(x, F, 'rx' , label = r'$Auslenkung \Delta x$')
plt.plot(line1, test_func(line1, *params), '-', label = r'Ausgleichsgerade')
plt.xlabel(r'x')
plt.ylabel(r'F')
plt.legend(loc = 'best')
plt.show()
fig.savefig('demo.png', bbox_inches='tight')