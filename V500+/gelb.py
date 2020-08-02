import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-1.00,-0.90,-0.80,-0.70,-0.66,-0.5,-0.4,-0.3,-0.2,-0.1,0.02,0.1	 ,0.2	 ,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1	 ,1.1,2	 ,3	 ,4	 ,5	 ,7	 ,9	 ,11	 ,15	 ,17	 ,17.5,19	 ])
y=np.array([0.000,0.000,0.000,0.000,0.000,0.000,0.045,0.045,0.063,0.110,0.141,0.173,0.205,0.237 ,0.268 ,0.293 ,0.316 ,0.332 ,0.354 ,0.367 ,0.387 ,0.400 ,0.469 ,0.524 ,0.566 ,0.583 ,0.632 ,0.648 ,0.663 ,0.693 ,0.693 ,0.707 ,0.707 ])

x1=np.array([-0.5,-0.4,-0.3,-0.2,-0.1,0.02,0.1	 ,0.2	 ,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])


y1=np.array([0.000,0.045,0.045,0.063,0.110,0.141,0.173,0.205,0.237 ,0.268 ,0.293 ,0.316 ,0.332 ,0.354 ,0.367 ,0.387 ])

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
plt.savefig('build/gelb.pdf')

