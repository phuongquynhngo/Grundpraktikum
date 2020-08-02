import numpy as np
import matplotlib.pyplot as plt



t, T7, T1, T2, T3, T4, T5, T6, T8 =np.loadtxt('werte1.txt', unpack=True)
t=t

plt.plot(t, T1, '-', label='Messdaten zu T1 (Messing, breit)')
plt.plot(t, T4 , '-', label='Messdaten zu T4 (Messing, klein )')
plt.xlabel(r'$t \,\, / \,\, \mathrm{s}$')
plt.ylabel(r'$T \,\, / \,\, \mathrm{°C}$')
plt.legend(loc='best')
plt.xlim(0,2000)
#plt.show()
plt.savefig('build/Diagramm11.pdf')
