import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math


x=np.array([15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360,375,390,405,420,435,450,465,480,495,510,525,540,555,570,585,600,615,630,645,660])
y=np.array([6.492,6.360,6.146,5.971,5.694,5.505,5.328,5.112,4.977,4.779,4.645,4.443,4.277,4.205,3.971,3.808,3.893,3.830,3.528,3.369,3.403,3.220,3.369,3.435,3.297,3.498,2.642,3.334,3.260,3.369,2.568,2.836,3.137,3.137,2.947,3.046,2.775,2.568,3.046,2.307,2.947,2.488,1.798,2.307 ])

x1=np.array([15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240])
y1=np.array([6.492,6.360,6.146,5.971,5.694,5.505,5.328,5.112,4.977,4.779,4.645,4.443,4.277,4.205,3.971,3.808])
x2=np.array([255,270,285,300,315,330,345,360,375,390,405,420,435,450,465,480,495,510,525,540,555,570,585,600,615,630,645,660])
y2=np.array([3.893,3.830,3.528,3.369,3.403,3.220,3.369,3.435,3.297,3.498,2.642,3.334,3.260,3.369,2.568,2.836,3.137,3.137,2.947,3.046,2.775,2.568,3.046,2.307,2.947,2.488,1.798,2.307 ])



def test_func1(x1, a1,b1 ):
    return -a1*x1+b1

params1, params1_convariance = curve_fit(test_func1, x1, y1)
errors1 = np.sqrt(np.diag(params1_convariance))
print(params1)
print('a1:', params1[0], '+-', errors1[0])
print('b1:', params1[1], '+-', errors1[1])



def test_func2(x2, a2,b2 ):
    return -a2*x2+b2

params2, params2_convariance = curve_fit(test_func2, x2, y2)
errors2 = np.sqrt(np.diag(params2_convariance))
print(params2)
print('a2:', params2[0], '+-', errors2[0])
print('b2:', params2[1], '+-', errors2[1])




plt.plot(x1, test_func1(x1, *params1), 'r-', label=r'Ausgleichungsgerade')
plt.plot(x2, test_func2(x2, *params2), 'b-', label=r'Ausgleichungsgerade')
plt.plot(x, y, 'x',color ='grey', label=r'Messwerte')
plt.ylabel(r'$\text{ln}(N)$')
plt.xlabel(r'$t\,\, / \,\, \mathrm{s}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Rhodiumausgleichung.pdf')
