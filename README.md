# infografia-estadistica
Respaldo de Infografia hecho en Python para el pre-procesamiento de los datos y en R para la busqueda y prueba de hipotesis

## Pre-procesamiento en Python

Tal cual como es R-Studio para el lenguaje R, Python tiene un ambiente para ejecutar porciones de codigo asilados y con librerias para el procesamiento de dataframes, y conjuntos de datos, integrada: Jupyter Notebook. Es por esta razón que el pre-procesamiento de los conjuntos de datos originales los he hecho con Pytho en Jupyter, dado que es más sencillo realizar queries para la separación de datasets de acuerdo al tiempo, que fue, en gran medida, lo que separaba las muestras para la prueba de las hipotesis planteadas en el infograma.

Los datasets originales no pueden ser almacenados en este repositorio, pues pesan más de 100Mb y ese es el limite para archivos en esta plataforma git, es por eso que deben ser descargados por aparte y puestos dentro de la carpeta  "datasets".

Los datasets originales que usé se encuentran en el siguiente enlace: https://drive.google.com/drive/folders/1TU-1JuXIvto_Np3r0tL_aUXx3YaRRRFe?usp=sharing
Los cuales son: 

- "Casos Positivos Covid-19 en Colombia": fuente - Datos Abiertos Colombia.
- "days.csv" el conjunto de días transcurridos desde el 15 de junio de 2020 hasta el 13 de junio de 2021
- "reportes_diarios.csv": fuente - cuenta de Twitter Ministerio de la Salud de Colombia @MinSaludCol, recolectados por el bot "scrapper.py"

Todos los subconjuntos, productos del pre-procesamiento, están dentro de la carpeta "out" de este directorio

### Nota

Si desea realizar la verificación de lo hecho en Python puede ver el resumén en pdf "pre-procesamiento.pdf" o bien instalar Anaconda en su máquina y correr el archivo "infografia.ipynb" y darle play en cada celda, después de haber descargado los datsets de google-drive y haberlos puesto en la carpeta "datasets"

## Procesamiento de datos y prueba de hipotesis

El procesamiento de los datos, como la lectura y la selección de columnas o elementos se hizo en R Markdown, tal cual se realizó en los ejercicios del curso __Probabilidad y Estadística__ así mismo como la validación de hipotesis, el codigo se encuentra de forma detallada en pdf en el archivo "infografia_final.pdf" y el codigo completo para su revisión en el archivo "infografia_final.Rmd" como soporte del codigo en R que solicita en las especificaciones del trabajo final de este curso.

## Conclusiones

Lo aprendido en este curso fue de gran ayuda para mi y muy necesario, pues espero orientar mi carrera (Ingeniería de Sistemas y Computación) en la aplicación y desarrollo de Inteligencia Artificial, rama de mi carrera que tiene como fundamento principal la estadística en la mayoría de sus técnicas como el Machine-Learning, Big Data y Deep Learning.

Att: Rubén Darío Vargas Yandy - estudiante Probabilidad y Estadística (Grupo B)

## Infografia

![alt infografia-completa](https://github.com/ruben4181/infografia-estadistica/blob/master/CoronaVirus%20(1).jpg?raw=true)
