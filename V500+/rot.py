import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-0.23,-0.20,-0.15,-0.10,-0.05,0.000,0.050,0.100,0.150,0.200,0.250,0.300,0.350,0.400,0.450,0.500,0.550,0.600,0.650,0.700,0.750,0.800,0.850,0.900,0.950,1.000])
y=np.array([0.000,0.000,0.032,0.045,0.055,0.071,0.089,0.110,0.126,0.141,0.155,0.167,0.179,0.190,0.200,0.207,0.214,0.219,0.224,0.230,0.235,0.239,0.241,0.245,0.249,0.253])
x1=np.array([-0.23,-0.20,-0.15,-0.10,-0.05,0.000,0.050,0.100,0.150,0.200,0.250,0.300,0.350])
y1=np.array([0.000,0.000,0.032,0.045,0.055,0.071,0.089,0.110,0.126,0.141,0.155,0.167,0.179])

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
plt.savefig('build/rot.pdf')

