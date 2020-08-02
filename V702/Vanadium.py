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
y=np.array([175.08, 183.08, 136.08, 145.08,141.08,118.08,103.08,93.08 ,80.08 ,86.08 ,65.08 ,55.08 ,67.08 ,32.08 ,35.08 ,47.08 ,42.08 ,26.08 ,31.08 ,18.08 ,13.08 ,29.08 ,21.08 ,5.08  ,14.08 ,13.08 ,22.08 ,11.08 ,15.08 ,4.08  ,3.08  ,10.08 ,7.08  ,11.08 ,7.08  ,10.08 ,11.08 ,3.08  ,6.08  ,5.08  ,6.08  ])
yerr=np.array([13.232  ,13.531  ,11.665  ,12.045  ,11.878  ,10.866  ,10.153  ,9.648   ,8.949   ,9.278   ,8.067   ,7.422   ,8.190   ,5.664   ,5.923   ,6.861   ,6.487   ,5.107   ,5.575   ,4.252   ,3.617   ,5.393   ,4.591   ,2.254   ,3.752   ,3.617   ,4.699   ,3.329   ,3.883   ,2.020   ,1.755   ,3.175   ,2.661   ,3.329   ,2.661   ,3.175   ,3.329   ,1.755   ,2.466   ,2.254   ,2.466  ])


plt.errorbar(x, y, yerr, fmt='x', ecolor='y',label=r'Fehler von N', capthick=1)
plt.plot(x, y, 'x', label=r'Messwerte')
plt.ylabel(r'$N \,\, / \,\, \mathrm{Imp}$')
plt.xlabel(r'$t\,\, / \,\, \mathrm{s}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Vanadium.pdf')
