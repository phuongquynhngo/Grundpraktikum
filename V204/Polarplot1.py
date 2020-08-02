import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit
import math

f = np.array([ 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
y = np.array([0.9286, 0.9286, 0.9286, 0.8929, 0.8857, 0.8643, 0.6857, 0.5357, 0.4286, 0.3571, 0.3036, 0.2571, 0.2321, 0.2071, 0.1786, 0.0914, 0.0607, 0.0493, 0.0393, 0.0321, 0.0279, 0.0246, 0.0211, 0.0196, 0.0179, 0.0164, 0.0150, 0.0141, 0.0114])
Uc = np.array([2.6, 2.6, 2.6, 2.5, 2.48, 2.42, 1.92, 1.5, 1.2, 1, 0.85, 0.72, 0.65, 0.58, 0.5, 0.256, 0.17, 0.138, 0.11, 0.09, 0.078, 0.069, 0.059, 0.055, 0.05, 0.046, 0.042, 0.0396, 0.032])

U0 = 2.8 
U = Uc/U0
T= 1/f
y1 = y*1e-3
phi = (y1/T)*2*np.pi 

plt.polar(phi, U , 'rx', label=r'Messwerte')
RC = 0.00093288
x=np.linspace(0,15000,25000)
phi = np.arcsin(((x*RC)/(np.sqrt(1+(x*RC)**2))))
y = 1/(np.sqrt(1+x**2*(RC)**2))

plt.polar(phi , y , '-', label=r'Theoretische Werte')
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4], [r"$0$", r"$45°$", r"$90°$",r"$135°$", r"$180°$", r"$225°$", r"$270°$", r"$315°$" ])
plt.legend(loc='center left', bbox_to_anchor=(1.1, 0.5), borderaxespad=0.)
plt.tight_layout()

#plt.show() 
plt.savefig('build/Polarplot1.pdf')