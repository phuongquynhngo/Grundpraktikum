import numpy as np
import math
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp

f, U_S, U_Br = np.genfromtxt('wien.txt', unpack=True)
Omega = f/160
Verhaeltnis = U_Br/U_S

x=np.array([1.000, 0.3125, 0.375, 0.5, 0.625, 0.75, 0.7813, 0.8125, 0.8438, 0.875, 0.9063, 0.9375, 1.0313, 1.0625,1.0938, 1.125, 1.5625, 1.175, 1.25, 1.375, 1.5625, 1.875, 2.1875, 2.5, 3.125, 4.375, 6.25, 12.5, 18.75, 62.5])

y=np.array([0.0172, 0.2308, 0.2308, 0.1538, 0.1, 0.0654, 0.0615, 0.0538, 0.0358, 0.0285, 0.0231, 0.0162, 0.0192, 0.0227, 0.0258, 0.03, 0.0342, 0.0423, 0.0538, 0.0692, 0.0962, 0.1038, 0.15, 0.1731, 0.212, 0.256, 0.28, 0.316, 0.3115, 0.3077])
print(f'Omega= {Omega} \n Verhältnis={Verhaeltnis}')
#Messwerte Kurve
plt.plot(x, y, 'bx', label=r'Messdaten')

#Theoriekurve
z=(1/9 * ((Omega**2 -1)**2)/((1-(Omega)**2)**2 + 9* (Omega) **2))**(1/2)
print(f'z= {z}')
plt.plot(x, z, 'k-', label=r'Theoriekurve')

plt.xlabel(r'$ \Omega = \frac{\omega}{\omega_0}$')
plt.ylabel(r'$\frac{U_{Br}}{U_S}$')
plt.xscale('log')
plt.grid()
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('Plotwien.pdf')
np.savetxt("datenez.txt",z)
