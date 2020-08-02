import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([30,31,35,37,38,40])
y=np.array([3.101,3.207,3.668,3.892,3.993,4.225])
def gerade(x, a, b):
    return a*x+b

params, params_convariance = curve_fit(gerade, x, y)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])



plt.plot(x, gerade(x, *params), '-',color ='blue', label=r'Ausgleichungsgerade')
plt.plot(x, y, 'x', color ='red', label=r'Werte')
plt.ylabel(r'$\sqrt{E_K} \,\, / \,\, \mathrm{(\sqrt{keV})}$')
plt.xlabel(r'$Z$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Rydberg.pdf')
