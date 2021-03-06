Tabla de Contenidos
=================

   * [Gestor de inventario mediante Python](#gestor-de-inventario-mediante-python)
      * [Instalación](#instalación)
      * [Ficheros](#ficheros)
      * [Features](#features)
      * [Ejecución](#ejecución)
   * [Totalizador de operaciones](#totalizador-de-operaciones)
      * [Instalación](#instalación-1)
      * [Ficheros](#ficheros-1)
      * [Ejecución](#ejecución-1)
   * [To-Do](#to-do)
   * [Licencia](#licencia)
   * [Notas](#notas)


# Gestor de inventario mediante Python
> Gestiona el inventario de un fichero .txt o .csv, canalizando las operaciones de venta y reposición de los distintos productos. Tras la última operación vuelca el inventario final en un nuevo fichero con el mismo formato que el inventario de entrada.

## Instalación

Para el funcionamiento del programa los únicos requisitos son [Python3](https://www.python.org/) y la librería [Pandas](https://pandas.pydata.org/index.html). Para su Instalación basta con ejecutar el siguiente comando:


```shell
pip install pandas
```

Otra opción es instalar [Anaconda](https://www.anaconda.com/), una versión encapsulada de Python que ya dispone de la librería Pandas

## Ficheros

El programa necesita los siguientes ficheros para su funcionamiento:

- **gestion_inventario.py**: scritp de Python.
- **inventarioAlmacen(.txt o .csv)**: fichero en el que se encuentra la información del stock que hay en inventario. Se codifica de la siguiente manera.

![Codificación archivo inventario](/media/inventario.jpg)

- **VentasRepos(.txt o .csv)**: fichero que recoge las operaciones de venta o reposición. Se encuentra codificado de la siguiente forma:

![Codificación archivo operaciones](/media/ventasrepos.jpg)

> La creación del fichero VentasRepos se ha creado mediante Mockaroo para la generación de un fichero con una extensión considerable.

## Features

Actualmente cuenta con las siguientes funcionalidades:

* Lectura de ficheros .txt o .csv con la información referente al inventario y almacenamiento de ésta en un dataframe de pandas.
* Lectura de ficheros .txt o .csv con las distintas operaciones de reposición y ventas y almacenamiento de ésta en un dataframe de pandas.
* Realización de las distintas operaciones. En el caso de que sean ventas se reducirá la cuantía al número de existencias en la estantería de ese producto. Por el contrario, en el caso de que sea una reposición se sumarán a las existencias en ese momento del producto. Adicionalmente, se hacen las siguientes comprobaciones:
    - Si a la hora de realizar la venta la cantidad es superior a las existencias saltará un error y no se realizará dicha venta.
    - Si a la hora de realizar una reposición la cantidad a reponer es superior a la capacidad de la estantería de dicho producto, se producirá un error y no se realizará dicha reposición.
    - En el momento en que las existencias sean menores o iguales al umbral, se lanzará un aviso para que se reponga el stock.
* Por último, vuelca el estado final del inventario tras la última operación en un nuevo fichero .txt o .csv según el formato del archivo de entrada del inventario, de forma que se mantiene el mismo formato tanto en entrada como en salida.

## Ejecución

Para la puesta en marcha se debe ejecutar el siguiente comando en caso de lectura de archivos .txt:

```shell
python3 gestion_inventario.py inventarioAlmacen.txt VentasRepos.txt
```
Y el siguiente comando en caso de lectura de archivos .csv:

```shell
python3 gestion_inventario.py inventarioAlmacen.csv VentasRepos.csv
```

# Totalizador de operaciones
> Totaliza las ventas y reposiciones de los diferentes productos mediante una técnica __mapreduce__.


## Instalación

El único requisito,una vez instalado [Python3](https://www.python.org/), es instalar la librería [mrjob](https://pythonhosted.org/mrjob/). Se instala mediante el siguiente comando:


```shell
pip install mrjob
```

## Ficheros

Para su funcionamiento se requiere un fichero con la misma estructura que el fichero "VentasRepos.txt". En este caso se encuentra disponible el fichero **VentasReposMapReduce.txt**, cuya única diferencia con el anterior el número de filas disponibles (100 vs 1.000).

## Ejecución

Para su ejecución se debe lanzar el siguiente comando:

```shell
python totalizador_operaciones.py VentasReposMapReduce.txt
```
En el caso de que la información procesada se quiera volcar a un ficero en lugar de ser impresa en pantalla el comando será:

```shell
python totalizador_operaciones.py VentasReposMapReduce.txt > example.txt
```

# To-Do

- ~~Comentar las funciones.~~
- ~~Implementar mediante una técnica **_mapreduce_** y la librería [mrjob](https://pythonhosted.org/mrjob/) una funcionalidad que totalice las ventas y reposiciones para un determinado periodo.~~


# Licencia

Este proyecto se encuentra bajo la licencia [**_GNU General Public License v3.0_**](/LICENSE)


# Notas

TOC generado mediante [github-markdown-toc.](https://github.com/ekalinin/github-markdown-toc)
