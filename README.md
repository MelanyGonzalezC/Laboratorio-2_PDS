# Laboratorio-2_PDS
## Descripción del proyecto
Este proyecto implementa un código para estudiar la convolución en señales y sistemas, y la correlación para medir su similitud. A partir de una señal electromiográfica (EMG) de Physionet, se aplica la Transformada de Fourier para analizar sus componentes en el dominio de la frecuencia.





## Correlación entre señales 
Para la segunda parte del código, se evaluan la correlación de dos señales que en este caso son : 

•	x1[nTs]=cos(2π100nTs)

•	x2[nTs]=sin⁡(2π100nTs)

Ambas señales están definidas en el intervalo 0 ≤ n< 90 y tienen un período de muestreo Ts= 1.25ms. El objetivo es calcular la correlación entre ellas y analizar la representación gráfica de las señales y su correlación. 

### Señales y su Representación
Las señales x1[n] y x2[n] son funciones discretas en el tiempo, lo que significa que están definidas en instantes específicos nTs en lugar de un tiempo continuo. Dado que la función seno y coseno están desfasadas 90° en el dominio del tiempo, esperamos que sus valores no sean idénticos en los mismos puntos de muestreo. Como el muestreo se realiza con un intervalo fijo Ts, el tiempo efectivo para cada muestra es nTs, donde n varía de 0 a 8, lo que significa que estamos observando solo 9 muestras de la señal. Las funciones seno y coseno son funciones periódicas, lo que significa que repiten su comportamiento en intervalos regulares de tiempo.

### Correlación entre Señales
La correlación es una medida estadística que describe el grado en que dos señales o variables están relacionadas entre sí. En términos simples, nos dice qué tan similares son dos señales y cómo cambia esa similitud cuando una de ellas se desplaza en el tiempo. Matemáticamente, la correlación cruzada entre dos señales x1[n] y x2[n] se define como:

![image](https://github.com/user-attachments/assets/1a9b8ed5-ef1b-4292-a4ca-8ec4871007c6)

*Formula de correlación de señales*

(Si la correlación es alta en un valor de l, significa que una señal es similar a la otra cuando está desplazada en l. Si la correlación es baja o negativa, significa que las señales están desfasadas o son opuestas en ese desplazamiento.)

Existen diferentes tipos de correlación, dependiendo de cómo se analicen los datos:
+ Correlación cruzada: Cuando trabajamos con señales discretas o continuas en el tiempo, usamos la correlación cruzada para medir la similitud entre dos señales a lo largo del tiempo.
+ Correlación lineal: Se usa en estadística para medir la relación lineal entre dos variables. Se expresa mediante un número entre -1 y 1:



Esto se hará a partir del siguiente codigo para obtener las graficas de correlación de las señales seno y coseno.

![image](https://github.com/user-attachments/assets/6d238de2-cbb3-4d08-baf3-02d2ab8bb3ee)

*Codigo para obtener la correlación de las señales*

En primer lugar se define el período de muestreo Ts=1.25ms=1.25×10−3sTs y posteriormente se crea el vector n, que representa los índices de muestreo desde 0 hasta 8, luego se definen las señales mencionadas anteriormente.  Estas son señales trigonométricas con una frecuencia de 100 Hz. La diferencia entre ellas es un desfase de 90°, ya que seno y coseno están desfasados por naturaleza.

Por otra parte, se utiliza la función de np.correlate para calcular la correlación cruzada entre ambas señales. La correlación mide la similitud entre las señales a medida que una se desplaza respecto a la otra y por ultimo, se normaliza dividiendo por el valor máximo absoluto de la correlación, para que sus valores queden en el rango de [−1,1].  Se crea un vector lag que representa los valores de desplazamiento entre las señales, desde −8 hasta +8. Luego se crea la interfaz para graficar las señales de seno, coseno y la correlación de ambas.

### Grafica 1

![image](https://github.com/user-attachments/assets/f8ebb617-8700-4878-bc1d-f42a8901bf82)
*Grafica de las señales coseno y seno*

La primera gráfica muestra la evolución de x1[n] y x2[n]en el dominio del tiempo. Se observa que ambas señales oscilan entre -1 y 1, como se espera de funciones trigonométricas. x1[n] (coseno) empieza en 1 cuando n=0, mientras que x2[n](seno) comienza en 0 y por ultimo podemos notar que hay un desfase de 90∘ entre las señales, lo que significa que cuando una señal alcanza su máximo, la otra se encuentra en un valor intermedio. 

### Grafica 2

![image](https://github.com/user-attachments/assets/51949abb-e1c7-4709-977b-2187ca79ab9f)

*Grafica de la correlación cruzada entre x1[n] y x2[n]*

De la grafica podemos identificar que La correlación no es máxima en k=0, lo que indica que las señales no están perfectamente alineadas, la correlación es máxima en un cierto valor de k, lo que confirma el desfase de 90∘ entre ellas y valores negativos de correlación indican que en esos desplazamientos, las señales están en oposición de fase. Por lo tanto, el patrón de la correlación coincide con lo esperado para señales senoidales desfasadas en 90∘. La simetría de la gráfica refleja que la correlación entre seno y coseno es periódica.






## Transformada de Fourier

Para finalizar el código presentado realiza el procesamiento de una señal adquirida de la base de datos PhysioNet, incluyendo caracterización temporal, análisis espectral y estadísticos descriptivos. Para un mayor entendimiento se explicará cada una de las etapas realizadas para el procesamiento de la señal. 
En primera medida, para la descarga de la señal el código hace uso de la librería wfdb para leer un registro de señal electrocardiográfica (ECG) de PhysioNet. La señal cargada proviene de un archivo .dat con su correspondiente encabezado. hea. Se extraen los siguientes datos: La freecuencia de muestreo(fs), y la señal correspondiente a una derivacion del ECG.

    
![image](https://github.com/user-attachments/assets/058c54e8-fcbc-4ad7-810e-0beffdabf30b)










*Sección del código que permite cargar la señal, además de la librería.*




Luego de esto, para la caracterización de la señal ECG se calculan una serie de estadísticos descriptivos, los cuales son: 1). La duracion total, que se obtiene dividiendo la cantidad de muestras entre la frecuencia de muestreo. 2).Media y mediana, las cuales representan la tendencia central de la señal. 3).Desviacion estandar, mide la dispersión de la señal con respecto a la media y la 4). Desviación absoluta mediana (MAD): Representa la variabilidad de la señal de forma robusta ante valores atípicos. 

De acuerdo a esto se grafica la señal en función del tiempo para asi observar su comportamiento. 



![image](https://github.com/user-attachments/assets/5feffe90-46c1-4dc8-ae32-512134083efb)











*Señal ECG obtenida.*


Esta señal parece ruidosa y con picos irregulares, lo que puede indicar:Presencia de ruido (interferencias externas o movimiento del paciente), un ritmo cardíaco irregular (arritmias posibles si los picos no siguen un patrón normal) y un ruido de alta frecuencia. 
La señal presenta altos niveles de ruido, evidenciados por picos bruscos y variaciones que no corresponden a una señal ECG limpia, addemas de eso, Se observa un patrón de variaciones alrededor de 0 mV, con picos esporádicos más elevados, lo que sugiere una captación inestable de la señal cardíaca.
Teniendo en cuenta que una señal ECG típica debe mostrar ondas P, QRS y T, que representan la despolarización y repolarización del corazón, en esta imagen, debido al ruido, no es posible distinguir claramente estas ondas, pero es probable que la señal requiera procesamiento digital, como filtrado de ruido y eliminación de artefactos, para extraer la información.


![image](https://github.com/user-attachments/assets/ee4506e2-a945-45e8-9994-44ea9348dae7)








*Código para calculo de los estadísticos descriptivos en función del tiempo.*


Gracias al segmento de código anterior pudimos ver los siguientes resultados, que explican que la señal fue muestreada a 250 Hz durante aproximadamente 20 horas, con una media de -0.2533 y una mediana de -0.2300, lo que indica una ligera tendencia hacia valores negativos. La desviación estándar es 0.2065, reflejando una variabilidad moderada, mientras que la desviación absoluta mediana (MAD) es 0.0650, lo que sugiere una dispersión relativamente baja y estabilidad en la señal sin valores extremos significativos.

![image](https://github.com/user-attachments/assets/1d0dab6a-a61f-429c-8fc4-37f36e83ec6c)









*Resultados estadísticos descriptivos en función del tiempo.*


Posterior a esto, para analizar la señal en el dominio de la frecuencia, se calcula la Transformada de Fourier (FFT) utilizando scipy.fftpack.fft. Se grafican el espectro de magnitud: Representa la amplitud de las componentes frecuenciales de la señal y la densidad espectral de potencia: Muestra la distribución de la energía en función de la frecuencia.


![image](https://github.com/user-attachments/assets/cb0c0483-ac8a-4c2b-9de9-175d7152f500)










*Código utilizado para la transformada de Fourier y densidad espectral.*


Teniendo este código en cuenta se obtienen las siguientes graficas:



![image](https://github.com/user-attachments/assets/decadc97-0b25-4a74-b133-5b5ee43369fa)










*Gráficos de la transformada de Fourier y densidad espectral de potencia de la señal ECG.*



La primer grafica representa la Transformada de Fourier de la señal ECG donde se evidencia la magnitud de la señal en función de la frecuencia. Se observa un pico prominente en la zona cercana a 0 Hz, lo que indica que la señal tiene una componente de muy baja frecuencia dominante (posiblemente debido al componente DC o variaciones lentas). Después de este pico, hay pequeñas variaciones en el espectro hasta aproximadamente 125 Hz (la mitad de la frecuencia de muestreo, que es el límite del teorema de Nyquist).
La segunda grafica permite ver como se distribuye la potencia de la señal a cada frecuencia, se evidencia que la mayor parte de la energía esta en frecuencias bajas con concentración cerca de los 0Hz. 


Finalmente, se calcularon los estadísticos en función de la frecuencia: frecuencia media que es la media ponderada de la distribución espectral, la frecuencia mediana donde la mitad de la energía está contenida, desviacion estandar de la frecuencia que mide la dispersión de la energía en el dominio frecuencial y el histograma de frecuencias donde se grafica la distribución de energía en distintos rangos de frecuencia. 

Esto se logró gracias a esta parte del código:
![image](https://github.com/user-attachments/assets/0ace1a88-04a1-4f4c-b855-895602225e57)












*Código para estadísticos descriptivos en función de la frecuencia.*

![image](https://github.com/user-attachments/assets/c6a798d4-7946-4c1f-8f04-d3e3e2a25a11)











*Resultados de estadisticos en funcion d ela frecuencia.*




Se obtuvo los siguientes resultados que permiten ver cómo está distribuida la energía en las distintas frecuencias después de aplicar la Transformada de Fourier. La Frecuencia media: -0.00 Hz indica el centro de masa del espectro de frecuencias, la mayor parte de la energía está concentrada en frecuencias bajas, la frecuencia mediana: 0.00 Hz representa la frecuencia en la que la mitad de la energía total está distribuida por debajo y la otra mitad por encima. Al ser 0.00 Hz, indica que la señal tiene una gran cantidad de componentes en bajas frecuencias, esto es totalmente normal en ECG ya que este tiene ritmos cardíacos en un rango de 0.05 Hz a 40 Hz) y la Desviación estándar mide la dispersión de las frecuencias con respecto a la media. Un valor de 5.35 Hz significa que la mayor parte de la energía de la señal ECG se encuentra dentro de un rango de aproximadamente 5.35 Hz alrededor de la media.

Es importante tener en cuenta las diferencias de los estadísticos en cada dominio, por ejemplo, en el dominio del tiempo calcula valores como media, mediana y desviación estándar de la señal en función de su amplitud y tiempo, nos dice qué tan grande es la señal y cómo varía con el tiempo, mientras que, en el dominio de la frecuencia se centra en la distribución de energía en las distintas frecuencias de la señal y nos dice en qué frecuencias ocurre esa variación. 

Un estadístico importante es el histograma que para este caso tiene una distribución sesgada a la derecha o exponencial, el cual refleja que la mayor parte de la energía está concentrada en frecuencias muy bajas (cercanas a 0 Hz) y que a medida que la frecuencia aumenta, la densidad de potencia disminuye rápidamente, indicando que las altas frecuencias contienen poca energía, lo cual sugiere que la señal es predominantemente de baja frecuencia y que los componentes de alta frecuencia pueden ser ruido o artefactos.


![image](https://github.com/user-attachments/assets/50cd6b24-c1cc-4953-9eac-963e20db76b2)











*Histograma obttenido.*

## Requisitos:
°Python 3.9


°	Wfdb



°Numpy




°Matplotlib



°scipy.fftpack
°scipy.stats
°fft, fftfreq
°median_abs_deviation
°Archivos .dat y .hea
## Contactanos:
°est.mariajose.perez@unimilitar.edu.co




°est.melany.gonzalez@unimilitar.edu.co





°est.david.smoreno@unimilitar.edu.co
## Bibliografia:
*Guardado, R., & Vallín González, D. (2009). Aplicación del análisis tiempo-frecuencia para la detección del complejo QRS en señales electrocardiográficas. LACCEI. https://laccei.org/LACCEI2009-Venezuela/p117.pdf






•  González Villada, M. (2009). Análisis de señales electrocardiográficas (ECG) con isquemia. Universidad de Manizales. https://ridum.umanizales.edu.co/xmlui/bitstream/handle/20.500.12746/156/180_Gonzalez_Villada_Marcela_2009.pdf





•  Lorenzoro, J. (2015). Análisis de señales electrocardiográficas usando técnicas de procesamiento digital. Universitat Oberta de Catalunya. https://openaccess.uoc.edu/bitstream/10609/40186/6/jlorenzoroTFC0115memoria.pdf





•  Martínez, J. P., & Olmos, S. (2005). Densidad espectral de potencia de un ECG. ResearchGate. https://www.researchgate.net/figure/Densidad-Espectral-de-Potencia-de-un-ECG_fig1_228843161





•  Merck Manuals. (s.f.). Electrocardiografía - Trastornos cardiovasculares. Recuperado de https://www.merckmanuals.com/es-us/professional/trastornos-cardiovasculares/pruebas-y-procedimientos-cardiovasculares/electrocardiograf%C3%ADa












    

    
