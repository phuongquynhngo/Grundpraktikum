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
y=np.array([660.04,578.04,467.04,392.04,297.04,246.04,206.04,166.04,145.04,119.04,104.04,85.04,	72.04,	67.04,	53.04,	45.04,	49.04,	46.04,	34.04,	29.04,	30.04,	25.04,	29.04,	31.04,	27.04,	33.04,	14.04,	28.04,	26.04,	29.04,	13.04,	17.04,	23.04,	23.04,	19.04,	21.04,	16.04,	13.04,	21.04,	10.04,	19.04,	12.04,	 6.04,	10.04])
yerr=np.array([ 25.691,24.042,21.611,19.800,17.235,15.686,14.354,12.886,12.043,10.911,10.200,9.222,	8.488,	8.188,	7.283,	6.711,	7.003,	6.785,	5.834,	5.389,	5.481,	5.004,	5.389,	5.571,	5.200,	5.748,	3.747,	5.295,	5.103,	5.389,	3.611,	4.128,	4.800,	4.800,	4.363,	4.587,	4.005,	3.611,	4.587,	3.169,	4.363,	3.470,	2.458,	3.169 ])


plt.errorbar(x, y, yerr, fmt='x', ecolor='y',label=r'Fehler von N', capthick=1)
plt.plot(x, y, 'x', label=r'Messwerte')
plt.ylabel(r'$N \,\, / \,\, \mathrm{Imp}$')
plt.xlabel(r'$t\,\, / \,\, \mathrm{s}$')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('build/Rhodium.pdf')
