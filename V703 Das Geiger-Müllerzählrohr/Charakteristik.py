import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x=np.array([320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700])
y=np.array([161.200,161.483,159.667,163.950,164.767,167.350,166.600,165.717,166.583,166.333,166.433,166.000,170.317,171.067,169.567,167.250,172.500,171.500,169.183,168.500,170.917,169.183,172.517,169.733,168.950,169.767,169.517,169.517,170.883,172.800,172.750,170.400,172.300,174.883,174.450,177.333,182.317,185.983,192.450])
yerr=np.array([12.696,12.708,12.636,12.804,12.836,12.936,12.907,12.873,12.907,12.897,12.901,12.884,13.051,13.079,13.022,12.933,13.134,13.096,13.007,12.981,13.074,13.007,13.135,13.028,12.998,13.029,13.020,13.020,13.072,13.145,13.143,13.054,13.126,13.224,13.208,13.317,13.502,13.638,13.873])
t=np.array([370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650])
U=np.array([167.350,166.600,165.717,166.583,166.333,166.433,166.000,170.317,171.067,169.567,167.250,172.500,171.500,169.183,168.500,170.917,169.183,172.517,169.733,168.950,169.767,169.517,169.517,170.883,172.800,172.750,170.400,172.300,174.883])

def gerade(t, a, b):
    return a*t+b

params, params_convariance = curve_fit(gerade, t, U)
errors = np.sqrt(np.diag(params_convariance))
print(params)
print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])



plt.plot(t, gerade(t, *params), 'r-', label=r'Ausgleichungsgerade')

plt.errorbar(x, y, yerr, fmt='x', ecolor='y',label=r'Fehler von N', capthick=1)
plt.plot(x, y, 'x', label=r'Messwerte')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')
plt.xlabel(r'$U \,\, / \,\, \mathrm{V}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Charakteristik.pdf')
