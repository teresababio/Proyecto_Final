# Clasificación de señales de tráfico

El objetivo de este repositorio es construir una red neuronal que sea capaz de clasificar las señales de tráfico pasadas a través de imágenes. El conjunto de señales a estudiar ha sido obtenido de la base de datos *GTSRB - German Traffic Sign Recognition Benchmark* (https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) que contiene 43 tipos de señales de tráfico distintas alemanas. Véase [dict.py](https://github.com/teresababio/Proyecto_Final/tree/main/dict) para ver las distintas señales.

## Datos y Data Augmentation
Del enlace de Kaggle se emplearán las carpetas Test y Train.

- Train: contiene 43 carpetas, en las que cada una de ellas hay fotos de la señal correspodiente. Como el conjunto train para cada uno de los labels, se procedió a aumentar el número de fotos de aquellos grupos que menos tenían mediante la librería Augmentor.

-Test: carpeta que contiene las fotos para realizar el testeo de los modelos. En Test.csv se encuentran las soluciones de los grupos.

Todo se encuentra en el programa [datos_modelos.py](https://github.com/teresababio/Proyecto_Final/blob/main/datos/Untitled.ipynb)

## Modelos 

Para la clasificación de los modelos se han probado tres redes neuronales. Una de ellas es una red neuronal entrenada desde el principio con los datos sin aplicar el data augmentation.  La segunda es la misma red neuronal pero ya con la base de datos aumentada y la última consiste en tomar la red neuronal ya entrenenada MobileNetSmall y entrenar las últimas capas de esta para adaptarlo a nuestro problema. Para todas las redes neuronales las imágenes tienen que tener un tamaño de (32,32,3) y deben dividirse entre 255.

### Resultados
Cuando se ejecutó el modelo con  MobileNetSmall se obtenía que el modelo estaba sobreajustado. A continuación se presentan los resultados

|               | CNN           | CNN_AUG     | MOBILENETSMALL       |
| ------------- | ------------- | --------    |  -----------         |
|  Train        | 0.99          | 0.97        |       0.98           |
|  Test         | 0.98          | 0.97        |       0.06           |

## Ejemplo imágenes
Los modelos que se han guardados en la carpeta modelos finales. Se han probado con el dataset [German Traffic Sign Detection Benchmark](https://benchmark.ini.rub.de/gtsdb_dataset.html), que a diferencia con el anterior este contiene imágenes de carreteras con señales de tráfico. Entonces, se han tomado mediante los recuadrados indicados en gt.txt las señales y se han predecho su tipo. Véase el programa [pruebas_imagenes_carretera.ipynb](https://github.com/teresababio/Proyecto_Final/blob/main/imagenes_completas/prueba_imagenes_carretera.ipynb)
# Ejemplo video
El programa [video.ipynb](https://github.com/teresababio/Proyecto_Final/blob/main/Ejemplo_video/video.ipynb) incluye una función que para el video especificado se detecta las señales del vídeo y se clasifican. Almacenando el resultado en un nuevo vídeo que contiene las soluciones de la detección y clasificación.

![](./dict/result.gif)

# Streamlit 
Se ha creado una carpeta streamlit para la presentación del trabajo. Para ejecutarla solo hace falta correr lo siguiente
code = """ cd streamlit """

```bash
cd streamlit_multi
./run_streamlit.sh
```

# Requerimientos
En [requirements.txt](https://github.com/teresababio/Proyecto_Final/blob/main/requirements.txt) se recogen todas las librerías necesarias para ejecutar el proyecto.



