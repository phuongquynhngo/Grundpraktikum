import numpy as np
import matplotlib.pyplot as plt



t, T7 =np.loadtxt('Bragg.dat', unpack=True)


plt.plot(t, T7, '-',  color ='grey',  label=r'Verbindung')
plt.plot(t, T7, 'x',  color ='red', label=r'Messwerte')

plt.xlabel(r'$\theta_\text{GM} \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)} $')

plt.xlim(25.8,30.2)
plt.ylim(40,230)
plt.tight_layout()
plt.legend(loc='best')
#plt.show()

plt.savefig('build/Bragg.pdf')