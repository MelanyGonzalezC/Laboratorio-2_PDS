import numpy as np
import matplotlib.pyplot as plt
import wfdb
from scipy.fftpack import fft, fftfreq
from scipy.stats import median_abs_deviation

# Definir las señales h[n] y x[n]
h = np.array([5, 6, 0, 0, 6, 9, 5])
x = np.array([1, 0, 1, 3, 2, 5, 9, 7, 0, 4])

h1 = np.array([5, 6, 0, 0, 7, 1, 0])
x1 = np.array([1, 0, 1, 9, 9, 8, 3, 5, 4, 7])

h2 = np.array([5, 6, 0, 0, 6, 9, 2])
x2 = np.array([1, 0, 0, 0, 1, 5, 7, 1, 1, 5])

# Calcular la convolución
y = np.convolve(x, h)
y1 = np.convolve(x1, h1)
y2 = np.convolve(x2, h2)

# Generar los índices de la señal de salida
y_n = np.arange(len(y))
y_n1 = np.arange(len(y1))
y_n2 = np.arange(len(y2))

# Imprimir la señal resultante en la consola
print("Resultado de la convolución MAJO y[n]:")
print(y)
print("Resultado de la convolución MELANY y[n]:")
print(y1)
print("Resultado de la convolución SANTI y[n]:")
print(y2)

# Crear una sola figura con tres subgráficos
plt.figure(figsize=(12, 10))

# Primer gráfico
plt.subplot(3, 1, 1)
plt.stem(y_n, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolución de x[n] y h[n] - MAJO')
plt.grid()
for i, txt in enumerate(y):
    plt.text(y_n[i], y[i], str(txt), ha='center', va='bottom', fontsize=9, color='red')

# Segundo gráfico
plt.subplot(3, 1, 2)
plt.stem(y_n1, y1)
plt.xlabel('n')
plt.ylabel('y1[n]')
plt.title('Convolución de x1[n] y h1[n] - MELANY')
plt.grid()
for i, txt in enumerate(y1):
    plt.text(y_n1[i], y1[i], str(txt), ha='center', va='bottom', fontsize=9, color='red')

# Tercer gráfico
plt.subplot(3, 1, 3)
plt.stem(y_n2, y2)
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.title('Convolución de x2[n] y h2[n] - SANTI')
plt.grid()
for i, txt in enumerate(y2):
    plt.text(y_n2[i], y2[i], str(txt), ha='center', va='bottom', fontsize=9, color='red')

# Mostrar la figura con todas las gráficas
plt.tight_layout()
plt.show()

# Definir parámetros para la correlación
Ts = 1.25e-3  # Período de muestreo en segundos
n = np.arange(9)

# Definir señales x1[nTs] y x2[nTs]
x1_t = np.cos(2 * np.pi * 100 * n * Ts)
x2_t = np.sin(2 * np.pi * 100 * n * Ts)

# Calcular la correlación normalizada
correlation = np.correlate(x1_t, x2_t, mode='full')
correlation /= np.max(np.abs(correlation))  # Normalización a [-1, 1]
lag = np.arange(-len(x1_t) + 1, len(x1_t))

# Imprimir la correlación
print("Correlación normalizada entre x1[nTs] y x2[nTs]:")
print(correlation)

# Crear una sola figura con dos subgráficos
plt.figure(figsize=(12, 10))

# Graficar x1[nTs] y x2[nTs] en un solo gráfico
plt.subplot(2, 1, 1)
plt.plot(n, x1_t, marker='o', linestyle='-', label='x1[nTs] = cos(2π100nTs)')
plt.plot(n, x2_t, marker='s', linestyle='-', label='x2[nTs] = sin(2π100nTs)')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.title('Señales x1[nTs] y x2[nTs]')
plt.legend()
plt.grid()

# Graficar la correlación
plt.subplot(2, 1, 2)
plt.plot(lag, correlation, marker='o', linestyle='-')
plt.xlabel('Desplazamiento')
plt.ylabel('Correlación normalizada')
plt.title('Correlación entre x1[nTs] y x2[nTs]')
plt.grid()

# Ajustar diseño y mostrar la figura
plt.tight_layout()
plt.show()

# Cargar la señal ECG desde un archivo .dat y su encabezado .hea
record_name = "chf08"  
record = wfdb.rdrecord(record_name)
fs = record.fs  # Frecuencia de muestreo
signal = record.p_signal[:, 0]  

# Crear vector de tiempo en segundos
time = np.arange(len(signal)) / fs  

# Estadísticos descriptivos
time_duration = len(signal) / fs
mean_value = np.mean(signal)
median_value = np.median(signal)
std_dev = np.std(signal)
mad = median_abs_deviation(signal)

# Imprimir características de la señal
print("--- Caracterización de la señal ---")
print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Duración total: {time_duration:.2f} s")
print(f"Media: {mean_value:.4f}")
print(f"Mediana: {median_value:.4f}")
print(f"Desviación estándar: {std_dev:.4f}")
print(f"Desviación absoluta mediana (MAD): {mad:.4f}")

# Gráfico de la señal ECG en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(time, signal, label='ECG')
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.title("Señal ECG")
plt.legend()
plt.grid()
plt.show()

# Transformada de Fourier (FFT)
n = len(signal)
freqs = fftfreq(n, 1/fs)
fft_values = fft(signal)
power_spectrum = np.abs(fft_values) ** 2

# Graficar FFT y densidad espectral
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(freqs[:n//2], np.abs(fft_values[:n//2]))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("Transformada de Fourier de la señal ECG")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(freqs[:n//2], power_spectrum[:n//2])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral de potencia")
plt.title("Densidad espectral de la señal ECG")
plt.grid()

plt.tight_layout()
plt.show()

# Estadísticos en función de la frecuencia
mean_freq = np.sum(freqs * power_spectrum) / np.sum(power_spectrum)
median_freq = freqs[np.searchsorted(np.cumsum(power_spectrum), np.sum(power_spectrum) / 2)]
std_freq = np.sqrt(np.sum(((freqs - mean_freq) ** 2) * power_spectrum) / np.sum(power_spectrum))

# Imprimir estadísticas de frecuencia
print("--- Estadísticos en función de la frecuencia ---")
print(f"Frecuencia media: {mean_freq:.2f} Hz")
print(f"Frecuencia mediana: {median_freq:.2f} Hz")
print(f"Desviación estándar: {std_freq:.2f} Hz")

# Histograma de frecuencias
plt.figure(figsize=(12, 6))
plt.hist(freqs[:n//2], bins=50, weights=power_spectrum[:n//2], alpha=0.7, color='b', edgecolor='k')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad de potencia")
plt.title("Histograma de la distribución de frecuencias de la señal ECG")
plt.grid()
plt.show()
