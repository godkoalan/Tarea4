import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import integrate
from scipy import signal

# Se crea una lista vacía para guardar los bits que sean leídos del archivo 
# bits10.csv 
bits=[]

# Se leen los bits mediante la función csv.reader
with open("bits10k.csv") as datos:
    readdatos = csv.reader(datos, delimiter=',')
    for row in readdatos:
        bits.append(row[0])

# Se convierte cada bit en un número entero
for i,j in enumerate(bits):
    bits[i]=int(j)


################################ Inciso a) ####################################

# Número de bits
N = len(bits)

# Frecuencia de operación
f = 5000 # Hz

# Duración del período de cada símbolo (onda)
T = 1/f # 1 ms

# Número de puntos de muestreo por período
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, 50)

# Creación de la forma de onda de la portadora
sinus = np.sin(2*np.pi * f * tp)

# Visualización de la forma de onda de la portadora
plt.plot(tp, sinus, 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Onda portadora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('portadora.png')
plt.grid(True)
plt.show()


# Frecuencia de muestreo
fs = p/T # 50 kHz

# Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada Tx
senal = np.zeros(t.shape)

# Creación de la señal modulada OOK
for k, i in enumerate(bits):
    if i==1:
        senal[k*p:(k+1)*p] = 1 * sinus
    else:
        senal[k*p:(k+1)*p] = -1 * sinus
        

# Visualización de los primeros bits modulados
pb = 10
plt.figure()
plt.plot(senal[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.title('Señal modulada con BPSK')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('Tx.png')
plt.grid(True)
plt.show()

################################ Inciso b) ####################################

# Potencia instantánea
Pinst = senal**2

# Potencia promedio a partir de la potencia instantánea (W)
Ps = integrate.trapz(Pinst, t) / (N * T)
#print('La potencia promedio está dad por:', Ps)

################################ Inciso c) ####################################

def senalaruido(x):
    return Ps / (10**(x / 10))

# Relación señal-a-ruido deseada
snr = np.linspace(-2,3,6)

# Potencia del ruido para SNR y potencia de la señal dadas
Pn = senalaruido(snr)
    
# Desviación estándar del ruido
sigma = np.sqrt(Pn)

# Crear ruido (Pn = sigma^2)

ruido1 = np.random.normal(0, sigma[0], senal.shape)
ruido2 = np.random.normal(0, sigma[1], senal.shape)
ruido3 = np.random.normal(0, sigma[2], senal.shape)
ruido4 = np.random.normal(0, sigma[3], senal.shape)
ruido5 = np.random.normal(0, sigma[4], senal.shape)
ruido6 = np.random.normal(0, sigma[5], senal.shape)


# Simular "el canal": señal recibida
Rx1 = senal + ruido1
Rx2 = senal + ruido2
Rx3 = senal + ruido3
Rx4 = senal + ruido4
Rx5 = senal + ruido5
Rx6 = senal + ruido6

tp1=np.linspace(0,0.002, 500)

plt.figure()
plt.plot(tp1, Rx1[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=-2 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=-2.png')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(tp1, Rx2[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=-1 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=-1.png')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(tp1, Rx3[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=0 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=0.png')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(tp1, Rx4[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=1 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=1.png')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(tp1, Rx5[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=2 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=2.png')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(tp1, Rx6[0:pb*p], 'c', linewidth=2, alpha=0.6)
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.title('Señal con SRN=3 dB')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la señal')
plt.savefig('SRN=3.png')
plt.grid(True)
plt.show()

################################ Inciso d) ####################################

plt.figure()
f0, Pxx0 = signal.welch(senal, fs)
plt.semilogy(f0, Pxx0, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia de la señal original')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('densoriginal')
plt.grid(True)
plt.show()

plt.figure()
f1, Pxx1 = signal.welch(Rx1, fs)
plt.semilogy(f1, Pxx1, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=-2 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens-2')
plt.grid(True)
plt.show()

plt.figure()
f2, Pxx2 = signal.welch(Rx2, fs)
plt.semilogy(f2, Pxx2, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=-1 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens-1')
plt.grid(True)
plt.show()

plt.figure()
f3, Pxx3 = signal.welch(Rx3, fs)
plt.semilogy(f3, Pxx3, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=0 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens0')
plt.grid(True)
plt.show()

plt.figure()
f4, Pxx4 = signal.welch(Rx4, fs)
plt.semilogy(f4, Pxx4, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=1 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens1')
plt.grid(True)
plt.show()

plt.figure()
f5, Pxx5 = signal.welch(Rx5, fs)
plt.semilogy(f5, Pxx5, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=2 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens2')
plt.grid(True)
plt.show()

plt.figure()
f6, Pxx6 = signal.welch(Rx6, fs)
plt.semilogy(f6, Pxx6, 'c', linewidth=2, alpha=0.6)
plt.title('Densidad espectral de potencia para SNR=3 dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig('dens3')
plt.grid(True)
plt.show()

################################ Inciso e) ####################################

# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)

# Inicialización del vector de bits recibidos
bitsRx = np.zeros(len(bits))

# Decodificación de la señal por detección de energía

for k, b in enumerate(bits):
    Ep = np.sum(Rx1[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0
        
err1 = np.sum(np.abs(bits - bitsRx))
Ber1 = err1/N*100

bitsRx = np.zeros(len(bits))
       
for k, b in enumerate(bits):
    Ep = np.sum(Rx2[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err2 = np.sum(np.abs(bits - bitsRx))
Ber2 = err2/N*100

bitsRx = np.zeros(len(bits))
       
for k, b in enumerate(bits):
    Ep = np.sum(Rx3[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err3 = np.sum(np.abs(bits - bitsRx))
Ber3 = err3/N*100

bitsRx = np.zeros(len(bits))
       
for k, b in enumerate(bits):
    Ep = np.sum(Rx4[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err4 = np.sum(np.abs(bits - bitsRx))
Ber4 = err4/N*100

bitsRx = np.zeros(len(bits))
       
for k, b in enumerate(bits):
    Ep = np.sum(Rx5[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err5 = np.sum(np.abs(bits - bitsRx))
Ber5 = err5/N*100

bitsRx = np.zeros(len(bits))
        
for k, b in enumerate(bits):
    Ep = np.sum(Rx6[k*p:(k+1)*p] * sinus)
    if Ep > 0.5*Es:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0
        
err6 = np.sum(np.abs(bits - bitsRx))
Ber6 = err6/N*100

################################ Inciso e) ####################################

Berarray=[]
Berarray.append(Ber1)
Berarray.append(Ber2)
Berarray.append(Ber3)
Berarray.append(Ber4)
Berarray.append(Ber5)
Berarray.append(Ber6)

Berarray = np.array(Berarray)

plt.figure()
plt.plot(snr, Berarray, 'c', linewidth=2, alpha=0.6)
plt.title('SNR vs BER')
plt.xlabel('SNR')
plt.ylabel('BER')
plt.savefig('SNRvsBER')
plt.grid(True)
plt.show()
