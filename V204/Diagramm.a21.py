import numpy as np
import matplotlib.pyplot as plt



t, T1, T2, T3, T4, T5, T6, T7, T8 =np.loadtxt('werte2.txt', unpack=True)
t=2*t

plt.plot(t, T1, '-', label='Messdaten zu T1')
plt.plot(t, T2 , '-', label='Messdaten zu T2')
plt.xlabel(r'$t \,\, / \,\, \mathrm{s}$')
plt.ylabel(r'$T \,\, / \,\, \mathrm{°C}$')
plt.legend(loc='best')
plt.xlim(0,2000)
#plt.show()
plt.savefig('build/Diagramm.a21.pdf')
