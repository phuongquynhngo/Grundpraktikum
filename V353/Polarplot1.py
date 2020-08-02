import matplotlib as mpl 
import numpy as np 

import matplotlib.pyplot as plt 
from scipy.stats import sem
import scipy.constants as const 
from scipy import optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

f = np.array([100, 150, 400, 600, 800, 1000, 1200, 1400, 1500, 2000, 5000, 7000, 9000, 11000])
y = np.array([0.7, 0.6, 0.3, 0.2, 0.18, 0.14, 0.12, 0.1, 0.1, 0.07, 0.03, 0.02, 0.016, 0.015])
Uc = np.array([2, 1.6, 0.75, 0.56, 0.28, 0.28, 0.28, 0.28, 0.28, 0.14, 0.07, 0.028, 0.014, 0.012])

U0 = 10
U1 =4.5*Uc/U0 
U = Uc/U0
T= 1/f
y1 = y*1e-3
phi = (y1/T)*2*np.pi 

plt.polar(phi, U , 'xr', label=r'$\text{Messwerte} \; \phi $ ')
plt.polar(phi, U1 , 'xg', label=r'$\text{Messwerte Angepasst} \; \phi $ ')
RC = 6.7*1e-3
x = np.linspace(0, 5000, 10000)
phi = np.arcsin(((x*RC)/(np.sqrt(1+x**2*(RC)**2))))
y= 1/(np.sqrt(1+x**2*(RC)**2))


plt.polar(phi, y, 'b-', label=r'$\text{Messwerte} \; U_C \ /\ U_0 $')
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4], [r"$0$", r"$45°$", r"$90°$",r"$135°$", r"$180°$", r"$225°$", r"$270°$", r"$315°$" ]

plt.tight_layout()

plt.savefig('build/Polarplot1.pdf')