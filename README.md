![image](https://github.com/ariigat0/G.I-JOE-Compiladores/assets/70560259/6f14f275-44a7-4397-994f-4df941601ba9)

# G.I-JOE-Compiladores

## Evidencia Final Compiladores: Desarrollo de herramienta de soporte al proceso de análisis de imágenes

<br> Ariadne Alvarez Reyes | A01652080
<br> Diego Corrales Pinedo | A01781631
<br> Salvador Salgado Normandia | A01422874

# Herramienta para Diseñar Flujos de Trabajo con Imágenes y Traducción

### Objetivo

El objetivo de este proyecto es implementar una herramienta que facilite el diseño de flujos de trabajo con imágenes mediante el uso de un traductor. La herramienta integrará funcionalidades de filtrado, procesamiento y análisis de imágenes utilizando OpenCV, permitiendo la ejecución de secuencias de comandos y la exportación de resultados.

## Introducción

Los traductores juegan un papel fundamental en la automatización y optimización de tareas para programadores en diversos campos. En este proyecto, combinamos el poder del lenguaje con herramientas de procesamiento de imágenes para asistir a los desarrolladores en la generación de flujos de trabajo eficientes y de alto nivel conceptual. La implementación de esta herramienta ofrece una ventaja competitiva y operativa al permitir la generación de vistas y cadenas de procesamiento que de otro modo no estarían disponibles.

## Desarrollo

Este entregable consiste en el desarrollo y demostración de una herramienta que cumpla con los siguientes requisitos:

- Facilitar el acceso a las funciones de filtrado y procesamiento de imágenes de OpenCV.
- Implementar flujos de transformaciones en imágenes mediante secuencias del lenguaje.
- Permitir la ejecución de bloques completos de tareas leídos desde archivos.
- Exportar los resultados del procesamiento de una imagen en un archivo de salida.
  -Ejecutar funciones para el análisis de imágenes, como histogramas, enmascaramiento o la separación de subáreas.

## Método

Partiendo del código base proporcionado en clase, se desarrollará una herramienta que facilite el análisis y producción de imágenes según los requisitos del Reto del Módulo.

## Características de entrega:

1. Repositorio público en Github/GitLab, etc.
2. Instrucciones detalladas para la instalación y ejecución del proyecto.
3. Conjunto de pruebas que cubran todas las reglas de la gramática implementada, todas las funciones que no provengan de bibliotecas externas y todos los caminos de ejecución del árbol. Además, el código deberá implementar funcionalidades adicionales a las presentadas en clase.

A continuación, se detallan las opciones disponibles junto con el puntaje asignado a cada una. Para considerar el código como completo (100), se deberá seleccionar una combinación de opciones que sume 100 y demostrar su correcta implementación:

| Características                                                                                                                    | Encargado        | Puntaje |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| Aceptar None como valor de la gramática para inicialización de variables                                                           | Diego Corrales   | 5       |
| Implementación de visualización de histogramas con opencv                                                                          | Ari Alvarez      | 10      |
| Aceptar cualquier función de numpy para manejo de matrices como np.where, np.mean, np.std. Al menos 9 de ellas                     | Diego Corrales   | 10      |
| Aceptar archivos y ejecutar el contenido                                                                                           | Diego Corrales   | 15      |
| Implementar flujos de funciones (->) que solo reciban la imagen como parámetro (como show_images)                                  | Equipo           | 15      |
| Implementación de un algoritmo complejo como herramienta en el lenguaje: WaterShed,                                                | Ari Alvarez      | 25      |
| Implementación de flujos que sean agregaciones: b = img -> blur(12) -> mean() como último paso. Estas funciones son parte de numpy | Salvador Salgado | 25      |
| **Total**                                                                                                                          |                  | **105** |

Para ver la documentación de las características implementadas, visitar los siguientes documentos:

- [Aceptar None para Inicialización de Variables](AceptarNone.md)
- [Visualización de Histogramas con OpenCV](Histograma_opencv.md)
- [Aceptar Funciones de Numpy](AceptarNumpy.md)
- [Aceptar Archivos y Ejecutar el Contenido](AceptarArchivos.md)
- [Implementar Flujos de Funciones](Flujos.md)
- [Implementación de un Algoritmo Complejo: WaterShed](Algoritmo_WaterShed.md)
- [Implementación de Flujos que sean Agregaciones]()

## Reglas de la Gramática Implementada

A continuación se listan las reglas de la gramática implementada en `translator.py`:

```markdown
assignment -> VARIABLE EQUAL expression
            | VARIABLE EQUAL flow
            | expression

flow -> VARIABLE CONNECT flow_functions

flow_functions -> flow_function_call CONNECT flow_functions
                | flow_function_call

flow_function_call -> VARIABLE LPAREN params RPAREN

assignment_aggregation -> VARIABLE EQUAL aggregation

aggregation -> NUMBER CONNECT aggregation_functions

aggregation_fucntions -> aggregation_function_call CONNECT aggregation_functions
                        |aggregation_function_call

aggregation_call -> NUMBER LPAREN params RPAREN

expression -> term
            | string_def
            | expression PLUS term
            | expression MINUS term

string_def -> STRING

term -> exponent
      | term TIMES exponent
      | term DIV exponent

exponent -> factor
          | factor EXP factor

factor -> NUMBER
        | VARIABLE
        | LPAREN expression RPAREN
        | function_call

function_call -> VARIABLE LPAREN RPAREN
               | VARIABLE LPAREN params RPAREN

params -> params COMMA expression
        | expression
```

## Ejecución y ejemplos

### Instalación

Se puede instalar el programa haciendo una copia local del presente repositorio:
`git clone https://github.com/ariigat0/G.I-JOE-Compiladores.git`

### Ejecución

En una línea de comando, posicionarse en la carpeta base del repositorio y correr:
`python translator.py`

Se ejecutará el translator y mostrará:

```markdown
Translator v1.0

>
```

Ahora se pueden escribir instrucciones para ser ejecutadas por el translator.

> **_NOTA:_** Se requiere de Python para correr `translator.py`. <br>
> **_NOTA:_** No se pueden escribir espacios en la entrada del translator.

### Ejemplos

Estos ejemplos cubren todas las reglas definidas en la gramática:

#### Ejemplo 1

Comando:

```markdown
a=average(tuple(2,3,4))+33^54-87\*2+4/23
```

Grafo resultante:
<br>
![image](ImagenesReadme/Full1.png)

Resultado:

```markdown
Graph with 0 nodes and 0 edges
Graph with 1 nodes and 0 edges
Graph with 2 nodes and 0 edges
Graph with 3 nodes and 0 edges
Graph with 4 nodes and 0 edges
Graph with 5 nodes and 3 edges
Graph with 6 nodes and 4 edges
Graph with 7 nodes and 4 edges
Graph with 8 nodes and 4 edges
Graph with 9 nodes and 6 edges
Graph with 10 nodes and 8 edges
Graph with 11 nodes and 8 edges
Graph with 12 nodes and 8 edges
Graph with 13 nodes and 10 edges
Graph with 14 nodes and 12 edges
Graph with 15 nodes and 12 edges
Graph with 16 nodes and 12 edges
Graph with 17 nodes and 14 edges
Graph with 18 nodes and 16 edges
Graph with 19 nodes and 16 edges
Result 9.994308557022821e+81
```

#### Ejemplo 2

Comandos:

```markdown
a=3
b=a->sumAB(3)->sumAB(3)->sumAB(3)
```

Grafos resultantes:
<br>
![image](ImagenesReadme/Full2.1.png)
![image](ImagenesReadme/Full2.2.png)

Resultado:

```markdown
> a=3
> Graph with 0 nodes and 0 edges
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 0 edges
> Result 3
> b=a->sumAB(3)->sumAB(3)->sumAB(3)
> Graph with 0 nodes and 0 edges
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 0 edges
> Graph with 4 nodes and 2 edges
> Graph with 5 nodes and 2 edges
> Graph with 6 nodes and 2 edges
> Graph with 7 nodes and 4 edges
> Graph with 8 nodes and 4 edges
> Graph with 9 nodes and 4 edges
> Graph with 10 nodes and 8 edges
> Graph with 11 nodes and 8 edges
> Result 12
```

#### Ejemplo 3

Comandos:

```markdown
a=23^3-2+45-90/2
myPrint(None,a,2,3)
```

Grafos resultantes:
<br>
![image](ImagenesReadme/Full3.1.png)
![image](ImagenesReadme/Full3.2.png)

Resultado:

```markdown
> a=23^3-2+45-90/2
> Graph with 0 nodes and 0 edges
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 0 edges
> Graph with 4 nodes and 2 edges
> Graph with 5 nodes and 2 edges
> Graph with 6 nodes and 4 edges
> Graph with 7 nodes and 4 edges
> Graph with 8 nodes and 6 edges
> Graph with 9 nodes and 6 edges
> Graph with 10 nodes and 6 edges
> Graph with 11 nodes and 8 edges
> Graph with 12 nodes and 10 edges
> Graph with 13 nodes and 10 edges
> Result 12165.0
> myPrint(None,a,2,3)
> Graph with 0 nodes and 0 edges
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 0 edges
> Graph with 4 nodes and 0 edges
> Graph with 5 nodes and 0 edges
> Printing: None 12165.0 2 3
> Result None
```

#### Ejemplo 4

Comandos:

```markdown
a=load("cv.jpg")
b= a->blur(15)
c=b->mean() // c=mean(b)
```

Grafos resultantes:
<br>
![image](ImagenesReadme/Full4.1.png)
![image](ImagenesReadme/Full4.2.png)

Resultado:

```markdown
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 1 edges
> Graph with 4 nodes and 1 edges
> Result [[[ 6 14 44] > [ 7 11 39] > [11 12 32]
> ...
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 0 edges
> Graph with 4 nodes and 2 edges
> Graph with 5 nodes and 2 edges
> [[[ 12 17 25] > [ 12 17 25] > [ 11 16 25]
> ...
> Graph with 0 nodes and 0 edges
> Graph with 1 nodes and 0 edges
> Graph with 2 nodes and 0 edges
> Graph with 3 nodes and 1 edges
> Graph with 4 nodes and 1 edges
> Result 113.89563093256133
```

> **_NOTA:_** Para ver ejemplos específicos a las características implementadas, favor de ver su documentación. Esta se puede encontrar en las ligas arriba.

## Videos Individuales

Favor de visitar el siguiente documento para ver las ligas a los videos de reflexión individuales: <br>
[Videos de Reflexión Individuales](Videos_individuales.md)

## Referencias

<br> OpenCV: Histograms - 1 : Find, Plot, Analyze !!! (n.d.). https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
<br> OpenCV: Image Segmentation with Watershed Algorithm. (n.d.). https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html
<br> Numpy.Mean — NumPy V1.26 Manual. (s. f.). https://numpy.org/doc/stable/reference/generated/numpy.mean.html
```
