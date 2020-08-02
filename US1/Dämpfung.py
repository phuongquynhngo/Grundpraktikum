import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math


x1 =np.array([0,0.395])
y1 =np.array([1.585,0.09])
x2 =np.array([0,0.616])
y2 =np.array([1.602,0.045])

def func_exp1(x1, a1):
    return 1.585* np.exp(-x1*a1)

params1, params1_convariance = curve_fit(func_exp1, x1, y1)
errors1 = np.sqrt(np.diag(params1_convariance))
print(params1)
print('a1:', params1[0], '+-', errors1[0])

def func_exp2(x2, a2):
    return 1.602* np.exp(-x2*a2)

params2, params2_convariance = curve_fit(func_exp2, x2, y2)
errors2 = np.sqrt(np.diag(params2_convariance))
print(params2)
print('a2:', params2[0], '+-', errors2[0])

def funca(xa, adj1a,adj2a):
    return ((xa+adj1a) ** pwa) * adj2a

xa = [0,0.395] # two given datapoints to which the exponential function with power pw should fit
ya = [1.585,0.09]

pwa = 15
Aa = np.exp(np.log(ya[0]/ya[1])/pwa)
aa = (xa[0] - xa[1]*Aa)/(Aa-1)
ba = ya[0]/(xa[0]+aa)**pwa

xfa=np.linspace(0,0.7,50)
plt.plot(xfa, funca(xfa, aa, ba), 'r-', label="Fit-Kurve kleines Acrylzylinders ")

def funcb(xb, adj1b,adj2b):
    return ((xb+adj1b) ** pwb) * adj2b

xb = [0,0.616] # two given datapoints to which the exponential function with power pw should fit
yb = [1.602,0.045]

pwb = 15
Ab = np.exp(np.log(yb[0]/yb[1])/pwb)
ab = (xb[0] - xb[1]*Ab)/(Ab-1)
bb = yb[0]/(xb[0]+ab)**pwb

xfb=np.linspace(0,0.7,50)
plt.plot(xfb, funcb(xfb, ab, bb), 'b-', label="Fit-Kurve grosses Acrylzylinders ")



plt.plot(x1, y1, 'gx', label=r'Messwerte')
plt.plot(x2, y2, 'gx')
plt.ylabel(r'$ \text{Amplitude U}\,\, / \,\, \mathrm{V}$')
plt.xlabel(r'$ \text{Strecke x}\,\, / \,\, \mathrm{10^{-3} \cdot m}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Dämpfung.pdf')



