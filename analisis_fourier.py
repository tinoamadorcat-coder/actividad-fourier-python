
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from pathlib import Path

# ==========================================================
# ACTIVIDAD FORMATIVA 2
# SIMULACION Y ANALISIS DE SEÑALES CON FOURIER
# ==========================================================

# Las imagenes se guardaran junto a este archivo Python.
CARPETA_SALIDA = Path(__file__).resolve().parent
FRECUENCIA_MUESTREO = 1000
DURACION = 1.0

cantidad_muestras = int(FRECUENCIA_MUESTREO * DURACION)
t = np.arange(cantidad_muestras) / FRECUENCIA_MUESTREO
dt = 1 / FRECUENCIA_MUESTREO

print("=" * 60)
print("ACTIVIDAD FORMATIVA 2: ANALISIS DE FOURIER")
print("=" * 60)


# ==========================================================
# 1. GENERACION DE LAS TRES SEÑALES
# ==========================================================

# Senoide de 10 Hz
frecuencia = 10
senal_senoidal = np.sin(2 * np.pi * frecuencia * t)

# Pulso rectangular: vale 1 entre 0.2 y 0.4 segundos
senal_rectangular = np.where(
    (t >= 0.2) & (t < 0.4), 1.0, 0.0
)

# Funcion escalon: cambia de 0 a 1 en 0.5 segundos
senal_escalon = np.where(t >= 0.5, 1.0, 0.0)


# ==========================================================
# 2. FUNCION PARA CALCULAR Y GRAFICAR LA TRANSFORMADA
# ==========================================================

def analizar_fourier(senal, nombre, nombre_archivo):
    N = len(senal)

    # Calculo de la Transformada Rapida de Fourier
    transformada = fft(senal)
    frecuencias = fftfreq(N, d=dt)

    # Espectro unilateral para señales reales
    mitad = N // 2
    frecuencias_positivas = frecuencias[:mitad]
    magnitud = np.abs(transformada[:mitad]) / N

    # Se duplican las amplitudes positivas, excepto DC
    # y Nyquist, para conservar la amplitud de la señal.
    magnitud_positiva = 2 * magnitud
    magnitud_positiva[0] /= 2

    fase = np.angle(transformada[:mitad])

    # La fase de componentes casi nulos no es significativa.
    umbral = max(np.max(magnitud_positiva) * 0.01, 1e-12)
    mascara = magnitud_positiva > umbral

    fig, ejes = plt.subplots(3, 1, figsize=(11, 9))

    # Dominio del tiempo
    ejes[0].plot(t, senal, color="blue")
    ejes[0].set_title(f"{nombre}: dominio del tiempo")
    ejes[0].set_xlabel("Tiempo (segundos)")
    ejes[0].set_ylabel("Amplitud")
    ejes[0].grid(True)

    # Magnitud del espectro
    ejes[1].plot(
        frecuencias_positivas,
        magnitud_positiva,
        color="red"
    )
    ejes[1].set_title("Magnitud del espectro")
    ejes[1].set_xlabel("Frecuencia (Hz)")
    ejes[1].set_ylabel("Magnitud")
    ejes[1].set_xlim(0, 100)
    ejes[1].grid(True)

    # Fase del espectro
    ejes[2].plot(
        frecuencias_positivas[mascara],
        fase[mascara],
        "o",
        markersize=3,
        color="green"
    )
    ejes[2].set_title("Fase del espectro")
    ejes[2].set_xlabel("Frecuencia (Hz)")
    ejes[2].set_ylabel("Fase (radianes)")
    ejes[2].set_xlim(0, 100)
    ejes[2].grid(True)

    fig.tight_layout()
    ruta = CARPETA_SALIDA / nombre_archivo
    fig.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    print(f"Imagen guardada: {ruta.name}")


# ==========================================================
# 3. ANALISIS DE LAS TRES SEÑALES
# ==========================================================

analizar_fourier(
    senal_senoidal,
    "Senal senoidal de 10 Hz",
    "01_senal_senoidal.png"
)

analizar_fourier(
    senal_rectangular,
    "Pulso rectangular",
    "02_pulso_rectangular.png"
)

analizar_fourier(
    senal_escalon,
    "Funcion escalon",
    "03_funcion_escalon.png"
)


# ==========================================================
# 4. PROPIEDAD DE LINEALIDAD
# ==========================================================

senal_a = np.sin(2 * np.pi * 10 * t)
senal_b = np.cos(2 * np.pi * 20 * t)

fft_a = fft(senal_a)
fft_b = fft(senal_b)
fft_suma = fft(senal_a + senal_b)

error_linealidad = np.max(
    np.abs(fft_suma - (fft_a + fft_b))
)

tolerancia = 1e-9
linealidad_correcta = error_linealidad < tolerancia

print("\n--- PROPIEDAD 1: LINEALIDAD ---")
print("La transformada de una suma debe ser la suma")
print("de las transformadas individuales.")
print(f"Error numerico: {error_linealidad:.12e}")
print("Resultado:", "CORRECTO" if linealidad_correcta else "REVISAR")


# ==========================================================
# 5. PROPIEDAD DE DESPLAZAMIENTO TEMPORAL
# ==========================================================

desplazamiento_muestras = 100
desplazamiento_segundos = desplazamiento_muestras * dt

# Desplazamiento circular de las muestras
senal_desplazada = np.roll(senal_a, desplazamiento_muestras)

fft_original = fft(senal_a)
fft_desplazada = fft(senal_desplazada)

# El desplazamiento cambia la fase, pero conserva la magnitud.
error_magnitud = np.max(
    np.abs(np.abs(fft_original) - np.abs(fft_desplazada))
)

desplazamiento_correcto = error_magnitud < tolerancia

print("\n--- PROPIEDAD 2: DESPLAZAMIENTO TEMPORAL ---")
print(f"Desplazamiento: {desplazamiento_segundos:.3f} segundos")
print("La magnitud del espectro debe permanecer igual.")
print(f"Error numerico: {error_magnitud:.12e}")
print(
    "Resultado:",
    "CORRECTO" if desplazamiento_correcto else "REVISAR"
)


# ==========================================================
# 6. ESCALAMIENTO EN FRECUENCIA
# ==========================================================

# Una senoide de 20 Hz oscila el doble de rapido que
# una senoide de 10 Hz durante el mismo intervalo.
senal_10_hz = np.sin(2 * np.pi * 10 * t)
senal_20_hz = np.sin(2 * np.pi * 20 * t)

fft_10_hz = np.abs(fft(senal_10_hz))
fft_20_hz = np.abs(fft(senal_20_hz))

frecuencias = fftfreq(cantidad_muestras, d=dt)
indices_positivos = np.where(frecuencias > 0)[0]

indice_10 = indices_positivos[
    np.argmax(fft_10_hz[indices_positivos])
]
indice_20 = indices_positivos[
    np.argmax(fft_20_hz[indices_positivos])
]

frecuencia_dominante_10 = frecuencias[indice_10]
frecuencia_dominante_20 = frecuencias[indice_20]

factor_escalamiento = (
    frecuencia_dominante_20 / frecuencia_dominante_10
)

print("\n--- PROPIEDAD 3: ESCALAMIENTO EN FRECUENCIA ---")
print(f"Frecuencia inicial: {frecuencia_dominante_10:.2f} Hz")
print(f"Frecuencia final: {frecuencia_dominante_20:.2f} Hz")
print(f"Factor observado: {factor_escalamiento:.2f}")
print(
    "Resultado:",
    "CORRECTO" if np.isclose(factor_escalamiento, 2.0)
    else "REVISAR"
)


# ==========================================================
# 7. GRAFICA COMPARATIVA DE LAS PROPIEDADES
# ==========================================================

fig, ejes = plt.subplots(3, 1, figsize=(11, 9))

# Comparacion de una señal y su desplazamiento
ejes[0].plot(t, senal_a, label="Original de 10 Hz")
ejes[0].plot(
    t, senal_desplazada,
    "--", label="Desplazada"
)
ejes[0].set_title("Desplazamiento temporal")
ejes[0].set_xlabel("Tiempo (segundos)")
ejes[0].set_ylabel("Amplitud")
ejes[0].legend()
ejes[0].grid(True)

# Comparacion de magnitudes: deben coincidir
ejes[1].plot(
    frecuencias[:cantidad_muestras // 2],
    np.abs(fft_original[:cantidad_muestras // 2]),
    label="Original"
)
ejes[1].plot(
    frecuencias[:cantidad_muestras // 2],
    np.abs(fft_desplazada[:cantidad_muestras // 2]),
    "--", label="Desplazada"
)
ejes[1].set_xlim(0, 50)
ejes[1].set_title("Magnitud antes y despues del desplazamiento")
ejes[1].set_xlabel("Frecuencia (Hz)")
ejes[1].set_ylabel("Magnitud FFT")
ejes[1].legend()
ejes[1].grid(True)

# Comparacion de frecuencias de 10 Hz y 20 Hz
ejes[2].plot(
    frecuencias[:cantidad_muestras // 2],
    fft_10_hz[:cantidad_muestras // 2],
    label="Senoide de 10 Hz"
)
ejes[2].plot(
    frecuencias[:cantidad_muestras // 2],
    fft_20_hz[:cantidad_muestras // 2],
    label="Senoide de 20 Hz"
)
ejes[2].set_xlim(0, 40)
ejes[2].set_title("Comparacion del escalamiento en frecuencia")
ejes[2].set_xlabel("Frecuencia (Hz)")
ejes[2].set_ylabel("Magnitud FFT")
ejes[2].legend()
ejes[2].grid(True)

fig.tight_layout()
ruta_comparacion = CARPETA_SALIDA / "04_propiedades_fourier.png"
fig.savefig(ruta_comparacion, dpi=150, bbox_inches="tight")
plt.show()
plt.close(fig)

print(f"\nImagen comparativa guardada: {ruta_comparacion.name}")


# ==========================================================
# 8. RESUMEN FINAL
# ==========================================================

print("\n" + "=" * 60)
print("RESUMEN DE COMPROBACIONES")
print("=" * 60)
print(f"Linealidad: {'APROBADA' if linealidad_correcta else 'REVISAR'}")
print(
    "Desplazamiento temporal: "
    f"{'APROBADO' if desplazamiento_correcto else 'REVISAR'}"
)
print(
    "Escalamiento en frecuencia: "
    f"{'APROBADO' if np.isclose(factor_escalamiento, 2.0) else 'REVISAR'}"
)
print("\nAnalisis de Fourier finalizado.")
print(f"Archivos guardados en: {CARPETA_SALIDA}")
