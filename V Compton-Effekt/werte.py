import numpy as np
import matplotlib.pyplot as plt



t, T7 =np.loadtxt('EmissionCu.dat', unpack=True)


plt.plot(t, T7, '-',  color ='black')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{Imp/s}$')

plt.xlim(8,25)
plt.ylim(0,6000)



plt.plot([20.2,20.2], [0,1599.0], color ='blue', linewidth=1.5, linestyle="--", label=r'$K_{\beta}\,\text{Linie}$')
plt.plot([22.5,22.5], [0,5050.0], color ='red', linewidth=1.5, linestyle="--", label=r'$K_{\alpha}\,\text{Linie}$')


plt.annotate('$20,2°/1599\,Imp/s$',xy=(20.2, 1599),  size=8,xycoords='data', xytext=(-40, 20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))

plt.annotate('$22,5°/5050\,Imp/s$',xy=(22.5, 5050), size=8,xycoords='data',xytext=(-40, 20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))
plt.legend(loc='best')
          
#plt.show()
plt.savefig('build/EmissionCu.pdf')


