## Modelos Probabilísticos de Señales y Sistemas - IE0405
### Tarea 4
### Alan Umaña Castillo
### B77773

#### Inciso a):

Inicialmente, se realiza la lectura de los bits suministrados mediante la función `csv.reader` de la librería *csv*. Dichos bits son convertidos a valores enteros mediante un ciclo y se guardan en un vector del mismo nombre. Posteriormente, se definen valores necesarios para realizar la simulación, como la frecuencia de la onda portadora, la cual es de 5000 *Hz*; el periodo de dicha onda, siendo éste de 20 *ms* y el número puntos de muestreo por período, definiéndose en 50.

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

Inicialmente, se define la **potencia instantánea** de la señal portadora como el cuadrado de dicha señal. Esto es:

![formula](https://render.githubusercontent.com/render/math?math=P_{inst}=sen^2(2\pi\f_pt))

Entonces, la **potencia promedio** se define como:


![formula](https://render.githubusercontent.com/render/math?math=P_{prom}=\frac{1}{2T}\int_{-T}^{T}P_{inst}dt)=
![formula](https://render.githubusercontent.com/render/math?math=\frac{1}{2T}\int_{-T}^{T}sen^2(2\pi\f_pt)dt)

Con el fin de calcular la integral anterior, se utiliza el módulo `integrate` de `SciPy`, dividiéndo el resultado de la integral entre el tiempo total, siendo este de de 200 *s*. De este proceso se obtuvo un valor de potencia promedio de 0.4900009800019598 *W*.

#### Inciso c):

Para realizar este inciso, se define una función en **Python** llamada `senalaruido`, la cual recibe un parámetro *x* que serían los valores de *SNR* y devuelve el valor de la *potencia del ruido* mediante la siguiente relación:

![formula](https://render.githubusercontent.com/render/math?math=P_{noise}=\frac{P_{signal}}{10^{\frac{SNR}{10}}})

Para los valores de *SNR* se cre un vectro de `NumPy` llamado `snr`, el cuál contendrá los valores solicitados de *SNR*. Una vez hecho esto, se calcula la desviación estándar al tomar la raíz cuadrada de cada uno de los valores de *potencia del ruido* calculados para los distintos *SNR*. Estos valores de deviación estándar se guardan en un vector llamado `sigma`. Cada valor de `sigma` se utiliza para generar un vector de *ruido* AWGN (additive white Gaussian noise), que posteriormente se suma entrada a entrada a la señal modulada. Estas señales con ruido se grafican y se presentan a continuación:

![SRN=-2](https://user-images.githubusercontent.com/66042916/86308162-b1954780-bbd5-11ea-811f-6a01b6ff4afb.png)

![SRN=-1](https://user-images.githubusercontent.com/66042916/86308158-b0641a80-bbd5-11ea-901c-805f128e2264.png)

![SRN=0](https://user-images.githubusercontent.com/66042916/86308151-ae01c080-bbd5-11ea-9dc6-c007499837b0.png)

![SRN=1](https://user-images.githubusercontent.com/66042916/86308155-afcb8400-bbd5-11ea-9996-019a5162a01c.png)

![SRN=2](https://user-images.githubusercontent.com/66042916/86308159-b0fcb100-bbd5-11ea-8a94-5374464633d7.png)

![SRN=3](https://user-images.githubusercontent.com/66042916/86308163-b22dde00-bbd5-11ea-8a5d-ab67baedc3a6.png)

#### Inciso d):

Para graficar la densidad espectral de potencia se utiliza la función `welch` del módulo `signal` de `SciPy`. Esta función recibe como argumento la señal a la cual se le desa graficar la densidad espectral de potencia y la frecuencia de dicha señal. Se grafica la densidad espectral de potencia de la señal original, además de las señales a las cuáles se les aplicó el AWGN. Los resultados obtenidos se muestran a continuación:

![densoriginal](https://user-images.githubusercontent.com/66042916/86308822-55cbbe00-bbd7-11ea-8179-378c01047e31.png)

![dens-2](https://user-images.githubusercontent.com/66042916/86308819-55332780-bbd7-11ea-81ef-d550cec103ec.png)

![dens-1](https://user-images.githubusercontent.com/66042916/86308817-549a9100-bbd7-11ea-8517-de7dd2aeb899.png)

![dens0](https://user-images.githubusercontent.com/66042916/86308811-5401fa80-bbd7-11ea-99cb-2dda54d5c098.png)

![dens1](https://user-images.githubusercontent.com/66042916/86308815-5401fa80-bbd7-11ea-9755-5ac6f594c2f5.png)

![dens2](https://user-images.githubusercontent.com/66042916/86308818-55332780-bbd7-11ea-9716-27864b58da0f.png)

![dens3](https://user-images.githubusercontent.com/66042916/86308821-55cbbe00-bbd7-11ea-98f1-373f67acdc51.png)











