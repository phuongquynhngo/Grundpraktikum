import numpy as np
import matplotlib.pyplot as plt

x, y =np.loadtxt('Rubidium.dat', unpack=True)




plt.plot(x, y, '-',  color ='grey',  label=r'Verbindung')
plt.plot(x, y, 'x',  color ='red', label=r'Messwerte')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')

plt.xlim(11,12.8)
plt.ylim(0,77)
plt.tight_layout()
plt.legend(loc='best')

plt.savefig('build/Rubidium.pdf')