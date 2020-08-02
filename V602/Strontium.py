import numpy as np
import matplotlib.pyplot as plt

x, y =np.loadtxt('Strontium.dat', unpack=True)




plt.plot(x, y, '-',  color ='grey', label=r'Verbindung')
plt.plot(x, y, 'x',  color ='red', label=r'Messwerte')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')

plt.xlim(10.2,12.3)
plt.ylim(20,210)
plt.tight_layout()
plt.legend(loc='best')

plt.savefig('build/Strontium.pdf')