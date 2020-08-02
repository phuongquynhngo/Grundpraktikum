import numpy as np
import matplotlib.pyplot as plt


def peak(x, c):
    return np.exp(-np.power(x - c, 2) / 16.0)

def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def half_max_x1(x, y):
    half1 = 2525
    signs = np.sign(np.add(y, -half1))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half1),
            lin_interp(x, y, zero_crossings_i[1], half1)]
def half_max_x2(x, y):
    half2 = 1599/2.0
    signs = np.sign(np.add(y, -half2))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half2),
            lin_interp(x, y, zero_crossings_i[1], half2)]



x, y =np.loadtxt('Emissionsspektrum.dat', unpack=True)




plt.plot(x, y, '-',  color ='grey')

plt.xlabel(r'$\theta \,\, / \,\, \mathrm{°}$')
plt.ylabel(r'$N \,\, / \,\, \mathrm{(Imp/s)}$')

plt.xlim(8,25)
plt.ylim(0,6000)


plt.plot([20.2,20.2], [0,1599.0], color ='green', linewidth=1.5, linestyle="--", label=r'$K_{\beta}\, \text{Linie}$')
plt.plot([22.5,22.5], [0,5050.0], color ='red', linewidth=1.5, linestyle="--", label=r'$K_{\alpha} \,\text{Linie}$')



# make some fake data

# find the two crossing points
hmx1 = half_max_x1(x,y)

# print the answer
fwhm1 = hmx1[1] - hmx1[0]
print("FWHM:{:.3f}".format(fwhm1), hmx1)

# a convincing plot
half1 = 2525

plt.plot(hmx1, [half1, half1], label=r'FWHM von $K_\alpha$\,Linie')

hmx2 = half_max_x2(x,y)

# print the answer
fwhm2 = hmx2[1] - hmx2[0]
print("FWHM:{:.3f}".format(fwhm2), hmx2)

# a convincing plot
half2 = 1599/2.0

plt.plot(hmx2, [half2, half2], label=r'FWHM von $K_\beta$\,Linie')

plt.annotate('$20,2°/1599 \, Imp/s$',xy=(20.2, 1599),  size=8,xycoords='data', xytext=(-40, 20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))

plt.annotate('$22,5°/5050 \, Imp/s$',xy=(22.5, 5050), size=8,xycoords='data',xytext=(-40, 20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))
plt.legend(loc='best')

          
#plt.show()
plt.savefig('build/EmissionCu.pdf')


