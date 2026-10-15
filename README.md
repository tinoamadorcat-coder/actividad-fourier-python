# Actividad formativa 2: Simulación y análisis de señales con la Transformada de Fourier

## Descripción del proyecto

Este proyecto simula y analiza diferentes señales utilizando Python y la Transformada de Fourier. Su propósito es observar el comportamiento de las señales en el dominio del tiempo y estudiar su representación en el dominio de la frecuencia.

## Objetivos

- Simular una señal senoidal, un pulso rectangular y una función escalón.
- Analizar el contenido frecuencial mediante la Transformada Rápida de Fourier (FFT).
- Representar gráficamente las señales y sus propiedades.
- Verificar las propiedades de linealidad, desplazamiento temporal y escalamiento en frecuencia.

## Tecnologías utilizadas

- Python
- NumPy
- Matplotlib
- SciPy

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `analisis_fourier.py` | Código fuente de la simulación y las comprobaciones. |
| `01_senal_senoidal.png` | Gráfica de la señal senoidal. |
| `02_pulso_rectangular.png` | Gráfica del pulso rectangular. |
| `03_funcion_escalon.png` | Gráfica de la función escalón. |
| `04_propiedades_fourier.png` | Comparación gráfica de las propiedades analizadas. |

## Requisitos e instalación

Se necesita Python y las siguientes bibliotecas:

```bash
pip install numpy matplotlib scipy
```

## Cómo ejecutar el programa

1. Descargar o clonar este repositorio.
2. Instalar las bibliotecas indicadas.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

```bash
python analisis_fourier.py
```

El programa genera las gráficas y muestra los resultados de las comprobaciones en la terminal.

## Resultados

Las comprobaciones realizadas reportaron los siguientes resultados:

- **Linealidad:** aprobada.
- **Desplazamiento temporal:** aprobado.
- **Escalamiento en frecuencia:** aprobado.

Los errores numéricos obtenidos en las comprobaciones de linealidad y desplazamiento temporal fueron prácticamente cero. La comparación de frecuencias mostró un cambio de 10 Hz a 20 Hz.

## Conclusión

La simulación permite observar cómo las señales pueden analizarse tanto en el dominio del tiempo como en el de la frecuencia. Las gráficas facilitan la comprensión de sus características y las comprobaciones numéricas permiten estudiar propiedades importantes de la Transformada de Fourier.

Este proyecto contribuye al aprendizaje práctico del análisis de señales mediante herramientas de programación científica en Python.

## Autor

Proyecto académico elaborado como parte de la Actividad formativa 2.
