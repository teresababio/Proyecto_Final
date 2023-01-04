# Clasificación de señales de tráfico

El objetivo de este repositorio es construir una red neuronal que sea capaz de clasificar las señales de tráfico pasadas a través de imágenes. El conjunto de señales a estudiar ha sido obtenido de la base de datos *GTSRB - German Traffic Sign Recognition Benchmark* (https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) que contiene 43 tipos de señales de tráfico distintas alemanas. Véase [dict.py](https://github.com/teresababio/Project_Penguin/blob/main/requirements.txt) para ver las distintas señales.

## Datos y Data Augmentation
Del enlace de Kaggle se emplearán las carpetas Test y Train.

- Train: contiene 43 carpetas, en las que cada una de ellas hay fotos de la señal correspodiente. Como el conjunto train para cada uno de los labels, se procedió a aumentar el número de fotos de aquellos grupos que menos tenían mediante la librería Augmentor.

-Test: carpeta que contiene las fotos para realizar el testeo de los modelos. En Test.csv se encuentran las soluciones de los grupos.

Todo se encuentra en el programa [datos_modelos.py](https://github.com/teresababio/Proyecto_Final/blob/main/datos/Untitled.ipynb)

## Modelos 

Para la clasificación de los modelos se han probado tres redes neuronales. Una de ellas es una red neuronal entrenada desde el principio con los datos sin aplicar el data augmentation.  La segunda es la misma red neuronal pero ya con la base de datos aumentada y la última consiste en tomar la red neuronal ya entrenenada MobileNetSmall y entrenar las últimas capas de esta para adaptarlo a nuestro problema. Para todas las redes neuronales las imágenes tienen que tener un tamaño de (30,30,3) y deben dividirse entre 255.

### Resultados

## Ejemplo real
Los modelos que se han guardados en la carpeta modelos finales. Se han probado con el dataset [German Traffic Sign Detection Benchmark](https://benchmark.ini.rub.de/gtsdb_dataset.html), que a diferencia con el anterior este contiene imágenes de carreteras con señales de tráfico. Entonces, se han tomado mediante los recuadrados indicados en gt.txt las señales y se han predecido su tipo. Así, se estaría probando el modelo en un caso real.

# Streamlit 

# Requerimientos




