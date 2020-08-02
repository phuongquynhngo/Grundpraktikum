import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math


x=np.array([30  ,60  ,90  ,120 ,150 ,180 ,210 ,240 ,270 ,300 ,330 ,360 ,390 ,420 ,450 ,480 ,510 ,540 ,570 ,600 ,630 ,660 ,690 ,720 ,750 ,780 ,810 ,840 ,870 ,900 ,930 ,960 ,990 ,1020,1050,1080,1110,1140,1170,1200,1230])
y=np.array([5.165,5.210,4.913,4.977,4.949,4.771,4.636,4.533,4.383,4.455,4.176,4.009,4.206,3.468,3.558,3.852,3.740,3.261,3.437,2.895,2.571,3.370,3.048,1.625,2.645,2.571,3.095,2.405,2.713,1.406,1.125,2.311,1.957,2.405,1.957,2.311,2.405,1.125,1.805,1.625,1.805 ])

x1=np.array([30  ,60  ,90  ,120 ,150 ,180 ,210 ,240 ,270 ,300 ,330 ,360 ,390 ,420 ,450 ,480 ,510 ,540 ,570 ,600 ,630 ,660])
y1=np.array([5.165,5.210,4.913,4.977,4.949,4.771,4.636,4.533,4.383,4.455,4.176,4.009,4.206,3.468,3.558,3.852,3.740,3.261,3.437,2.895,2.571,3.370])
def test_func(x1, a,b ):
    return -a*x1+b

params, params_convariance = curve_fit(test_func, x1, y1)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

plt.plot(x1, test_func(x1, *params), 'r-', label=r'Ausgleichungsgerade')
plt.plot(x, y, 'x', label=r'Messwerte')
plt.ylabel(r'$\text{ln}(N)$')
plt.xlabel(r'$t\,\, / \,\, \mathrm{s}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Vanadiumausgleichung.pdf')
