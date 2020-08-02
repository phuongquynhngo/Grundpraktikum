import matplotlib.pylot as plt 
import numpy as np

t,t1,t2,t3,t4,t5,t6,t7,t8 = np.loadtxt('werte2.txt', unpack = True)

t=t/2
plt.plot(t,t1, '-' ,label='T1')
plt.plot(t,t2, '-' ,label='T2')

plt.xlabel(r'$Zeit\,\, / \,\, s$')
plt.ylabel(r'$Temperatur \,\, / \,\, °CS')
plt.legend(loc='best')
plt.savefig('plott.pdf')

