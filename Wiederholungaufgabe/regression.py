import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math


#N, D, U =np.genfromtxt("data.csv",delimiter=";",unpack=True)
D=np.array([0, 6, 12, 18, 24, 30, 36, 42, 48])
U=np.array([-19.5, -16.1, -12.4, -9.6, -6.2, -2.4, 1.2, 5.1, 8.3])

def gerade(U, m, b):
    return m*U+b

params, params_convariance = curve_fit(gerade, U, D)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('m:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])


def test_func(U, m, b):
    return m * U + b



plt.plot(U, D, 'rx', label=r'Messwerte')
plt.plot(U, test_func(U, *params), '-', label=r'Ausgleichungskurve')
plt.xlabel(r'$U \,\, / \,\, \mathrm{V}$')
plt.ylabel(r'$D \,\, / \,\, \mathrm{mm}$')
plt.legend(loc='best')
plt.xlim(-20,10)
#plt.show()
plt.savefig('build/regression.pdf')



