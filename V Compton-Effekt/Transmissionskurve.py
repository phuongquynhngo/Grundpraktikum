import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit


T1, T2 =np.loadtxt('ComptonAl.txt', unpack=True)
T3, T4 =np.loadtxt('ComptonOhne.txt', unpack=True)

I1=(T2)/(1-90*10**(-6)*T2)
I2=(T4)/(1-90*10**(-6)*T4)
U=I1/I2
t=2*np.sin(T1*np.pi/180)*201.4
yerr=np.array([0.0571899,0.0535783,0.0512960,0.0498692,0.0486443,0.0466718,0.0450818,0.0440904,0.0430249,0.0410370,0.0395411,0.0386410,0.0371540,0.0363629,0.0352263,0.0337015,0.0328483,0.0324823,0.0313741,0.0305012,0.0292472,0.0284733,0.0279026,0.0269157,0.0264119,0.0256550,0.0249026,0.0242772,0.0237872,0.0230841,0.0223893])


def gerade(t, a, b):
    return a*t+b

params, params_convariance = curve_fit(gerade, t, U)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])



plt.plot(t, gerade(t, *params), 'r-', label=r'Ausgleichungsgerade')
plt.errorbar(t, U, yerr, fmt='x', ecolor='y',label=r'Fehler von T', capthick=1)
plt.plot(t, U, 'x', label=r'Messwerte')
plt.ylabel(r'$T(\lambda)$')
plt.xlabel(r'$\lambda \,\, / \,\, \mathrm{pm}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Transmissionskurve.pdf')
