import numpy as np 
x = np.genfromtxt('werteD.txt', unpack=True)
m=np.mean(x)
print(x)
print(f'Mittelwerte :{m}')
s=np.std(x)
print(f'Standardabweichung{s}')