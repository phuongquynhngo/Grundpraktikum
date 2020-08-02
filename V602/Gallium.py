import numpy as np
import matplotlib.pyplot as plt

x, y =np.loadtxt('Gallium.dat', unpack=True)




plt.plot(x, y, '-',  color ='grey',  label=r'Verbindung')
plt.plot(x, y, 'x',  color ='red', label=r'Messwerte')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')

plt.xlim(16.7,19.3)
plt.ylim(60,130)
# print( np.interp(17.45, x, y)) #find y of a given x, y monoton
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('build/Gallium.pdf')