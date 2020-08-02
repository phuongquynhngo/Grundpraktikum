import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([350,400,450,500,550,600,650,700])
y=np.array([114.364,150.075,255.748,295.537,368.225,475.471,500.334,584.567])
yerr=np.array([8.932,11.628,19.554,22.721,28.264,36.373,37.834,42.138])

def gerade(x, a, b):
    return a*x+b

params, params_convariance = curve_fit(gerade, x, y)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

plt.errorbar(x, y, yerr, fmt='x', ecolor='y',label=r'Fehler von Z', capthick=1)
plt.plot(x, gerade(x, *params), 'r-', label=r'Ausgleichungsgerade')
plt.plot(x, y, 'x', label=r'Messwerte')
plt.ylabel(r'$Z \,\, / \,\, \mathrm{10^{8}}$')
plt.xlabel(r'$U\,\, / \,\, \mathrm{V}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Zaehlrohrstroms.pdf')
