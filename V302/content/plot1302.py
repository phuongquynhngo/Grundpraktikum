import matplotlib.pyplot as plt
import numpy as np

v, U_Br = np.genfromtxt('wien.txt', unpack=True)

omega = v/120

plt.plot(omega, U_Br/4.36,'rx', label='Messwerte')
plt.xscale('log')
plt.xlim(-10,1000)
plt.ylabel(r'$(U_BR/U_S) $')
plt.xlabel(r'$\nu \ /\ \nu_0$')
plt.legend(loc='best')


def f(v):
   return np.sqrt((1/9)*(v**2-1)**2/((1-v**2)**2+9*v**2))

x_plot = np.linspace(0.01, 960000, 1000000)
plt.plot(x_plot/240, f(x_plot/240), 'b-', label=r'\text{Theoriekurve} $U_{Br} \ /\ U_s$', linewidth=0.5)
plt.xscale('log')
plt.xlim(-10,1000)
plt.ylabel(r'$U_{BR}/U_S$')
plt.xlabel(r'$\nu \ /\ \nu_0$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('Plot302.pdf')