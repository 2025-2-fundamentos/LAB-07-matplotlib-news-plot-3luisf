"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    def preparar_carpeta_de_graficos():
        """Garantiza que exista el directorio donde se guardarán los gráficos."""
        ruta_graficos = Path("files/plots")
        ruta_graficos.mkdir(parents=True, exist_ok=True)
        print(f"Carpeta '{ruta_graficos}' lista para uso.")

    preparar_carpeta_de_graficos()

    # Ajuste: corrección del nombre del color previamente escrito incorrectamente.
    paleta_colores = {
        'Newspaper': 'grey',
        'Radio': 'lightgrey',
        'Television': 'dimgray',
        'Internet': 'tab:blue',
    }

    # Nivel de superposición para las capas de dibujo.
    niveles_superposicion = {
        'Newspaper': 1,
        'Radio': 1,
        'Television': 1,
        'Internet': 2,
    }

    # Grosor asignado a cada serie para destacarlas de manera diferenciada.
    grosores_trazo = {
        'Newspaper': 2,
        'Radio': 2,
        'Television': 2,
        'Internet': 4,
    }

    # Carga del archivo que contiene los porcentajes de consumo de noticias.
    datos_medios = pd.read_csv("files/input/news.csv", index_col=0)

    # Creación de una nueva figura para la visualización.
    plt.figure(figsize=(10, 6))

    # Trazado de cada medio informativo.
    for etiqueta in datos_medios.columns:
        plt.plot(
            datos_medios[etiqueta],
            color=paleta_colores[etiqueta],
            label=etiqueta,
            zorder=niveles_superposicion[etiqueta],
            linewidth=grosores_trazo[etiqueta],
        )

    # Título de la gráfica para describir su contenido.
    plt.title("Evolución del acceso a noticias por tipo de medio")

    # Ajustes visuales del gráfico para un diseño más limpio.
    eje_actual = plt.gca()
    eje_actual.spines['top'].set_visible(False)
    eje_actual.spines['right'].set_visible(False)
    eje_actual.spines['left'].set_visible(False)
    eje_actual.get_yaxis().set_visible(False)

    # Marcado y anotación de los porcentajes iniciales y finales.
    for etiqueta in datos_medios.columns:
        inicio = datos_medios.index[0]
        fin = datos_medios.index[-1]

        # Punto inicial del registro
        plt.scatter(
            x=inicio,
            y=datos_medios[etiqueta].iloc[0],
            color=paleta_colores[etiqueta],
            zorder=niveles_superposicion[etiqueta],
        )

        plt.text(
            inicio - 0.2,
            datos_medios[etiqueta].iloc[0],
            f"{etiqueta}: {datos_medios[etiqueta].iloc[0]}%",
            ha='right',
            va='center',
            color=paleta_colores[etiqueta],
        )

        # Punto final del registro
        plt.scatter(
            x=fin,
            y=datos_medios[etiqueta].iloc[-1],
            color=paleta_colores[etiqueta],
            zorder=niveles_superposicion[etiqueta],
        )

        plt.text(
            fin + 0.2,
            datos_medios[etiqueta].iloc[-1],
            f"{etiqueta}: {datos_medios[etiqueta].iloc[-1]}%",
            ha='left',
            va='center',
            color=paleta_colores[etiqueta],
        )

    # Guardado final de la visualización en la carpeta correspondiente.
    plt.savefig("files/plots/news.png", bbox_inches="tight")
    plt.close()