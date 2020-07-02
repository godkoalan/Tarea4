## Modelos probabilísticos de Señales y Sistemas - IE0405
### Tarea 3
### Alan Umaña Castillo
### B77773

#### Inciso a):

Inicialmente, se realiza la lectura de los bits suministrados mediante la función *csv.reader* de la librería *csv*. Dichos bits son convertidos a valores enteros mediante un ciclo y se guardan en un vector del mismo nombre. Posteriormente, se definen valores necesarios para realizar la simulación, como la frecuencia de la onda portadora, la cual es de 5000 *Hz*; el periodo de dicha onda, siendo éste de 20 *ms* y el número puntos de muestreo por período, definiéndose en 50.

Una vez hecho esto, se grafica la señal portadora, la cual coresponde a una señal sinusoidal de 5000 *Hz* de frecuencia y una amplitud unitaria. Esta señal portadora está definida de la siguiente forma.

![formula](https://render.githubusercontent.com/render/math?math=S(t)=sen(2\pi\f_pt))

donde ![formula](https://render.githubusercontent.com/render/math?math=f_p) representa la frecuencia de la señal portadora.

Dicha señal se muestra en la siguiente figura:

![portadora](https://user-images.githubusercontent.com/66042916/86303737-f915d680-bbc9-11ea-95e9-d737e55b3ee7.png)

Ahora, la modulación **BPSK** se basa en un cambio de fase de 180° en la onda portadora, dependiendo de si se tiene un 1 ó un 0 en la señal modulada. Este cambio de fase se puede traducir fácilmente como una inversión de la señal portadora, por lo que se tendría que:

![formula](https://render.githubusercontent.com/render/math?math=S_1(t)=sen(2\pi\f_pt)), si el bit de la señal moduladora es 1.

![formula](https://render.githubusercontent.com/render/math?math=S_0(t)=-sen(2\pi\f_pt)), si el bit de la señal moduladora es 0.

La modulación se realiza mediante un ciclo en **Python**, tomando en cuenta las condiciones anteriormente mencionadas. 

![Tx](https://user-images.githubusercontent.com/66042916/86304457-1a77c200-bbcc-11ea-9ea4-bfaede3a7ea7.png)

En la figura anterior es posible apreciar la señal modulada para los primero 10 bits del arreglo dado en el archivo *bits10k.csv*, los cuales son (0, 1, 0, 1, 0, 1, 1, 0, 1, 0).

#### Inciso b):
























