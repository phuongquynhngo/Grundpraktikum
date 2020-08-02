import numpy as np
import matplotlib.pyplot as plt

x, y =np.loadtxt('Zink.dat', unpack=True)




plt.plot(x, y, '-',  color ='grey',  label=r'Verbindung')
plt.plot(x, y, 'x',  color ='red', label=r'Messwerte')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')

plt.xlim(17.7,19.8)
plt.ylim(50,110)
plt.tight_layout()
plt.legend(loc='best')

plt.savefig('build/Zink.pdf')