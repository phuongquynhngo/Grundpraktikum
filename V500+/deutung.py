import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([-19.14,-12.00,-10.00,-8.00	,-6.00	,-4.00	,-3.00	,-2.00	,-1.00,-0.90,-0.80,-0.70,-0.66,-0.5,-0.4,-0.3,-0.2,-0.1,0.02,0.1	 ,0.2	 ,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1	 ,1.1,2	 ,3	 ,4	 ,5	 ,7	 ,9	 ,11	 ,15	 ,17	 ,17.5,19	 ])
y=np.array([-0.020,-0.020,-0.020,-0.020,-0.020,-0.020,-0.020,-0.020,0.000	,0.000	,0.000	,0.000	,0.000	,0.   	,0.002	,0.002	,0.004	,0.012	,0.02	,0.03	,0.042	,0.056,0.072,0.086,0.100,0.110,0.125,0.135,0.150,0.160,0.220,0.275,0.320,0.340,0.4	,0.42	,0.44	,0.48	,0.48	,0.5	,0.5	])



plt.plot(x, y, 'rx', label=r'Messwerte')
plt.ylabel(r'$I\,\, / \,\, \mathrm{nA}$')
plt.xlabel(r'$U\,\, / \,\, \mathrm{V}$')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('build/deutung.pdf')