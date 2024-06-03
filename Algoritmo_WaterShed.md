# Implementación de un algoritmo complejo como herramienta en el lenguaje: WaterShed

# Reglas de la Gramática Implementada

## Cargar Imagen:

Se carga una imagen en color y se convierte a escala de grises.
- `cv2.imread('filename')` carga la imagen.
- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` convierte la imagen a escala de grises.

## Aplicar Umbral:

Se aplica un umbral binario inverso usando el método de Otsu.
- `cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)`

## Eliminación de Ruido:

Se elimina el ruido utilizando operaciones morfológicas (apertura).
- `cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)`

## Área Segura de Fondo:

Se obtiene la región segura de fondo mediante dilatación.
- `cv2.dilate(opening, kernel, iterations=3)`

## Área Segura de Primer Plano:

Se calcula la transformada de distancia y se aplica otro umbral.
- `cv2.distanceTransform(opening, cv2.DIST_L2, 5)`
- `cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)`

## Región Desconocida:

Se identifica la región desconocida restando las áreas seguras de primer plano del fondo.
- `cv2.subtract(sure_bg, sure_fg)`

## Marcadores para Watershed:

Se etiqueta el área segura de primer plano y se ajustan los marcadores.
- `cv2.connectedComponents(sure_fg)`
- Se ajustan los marcadores para que la región de fondo no sea cero.
- `markers = markers + 1`
- La región desconocida se marca con cero.
- `markers[unknown == 255] = 0`

## Aplicación del Algoritmo Watershed:

Se aplica el algoritmo Watershed.
- `cv2.watershed(image, markers)`

## Visualización de Resultados:

Se marcan los contornos de los objetos segmentados en la imagen original.
- `image[markers == -1] = [255, 0, 0]`

# Descripción de las Funciones Implementadas como Herramientas y Accesorios a la Gramática

## Cargar y Convertir Imagen:

- `cv2.imread()`: Carga la imagen.
- `cv2.cvtColor()`: Convierte la imagen a escala de grises.

## Aplicar Umbral y Eliminación de Ruido:

- `cv2.threshold()`: Aplica el umbral.
- `cv2.morphologyEx()`: Realiza operaciones morfológicas para eliminar ruido.

## Regiones Seguras de Fondo y Primer Plano:

- `cv2.dilate()`: Dilata la imagen para obtener el fondo.
- `cv2.distanceTransform()`: Calcula la transformada de distancia.
- `cv2.threshold()`: Aplica un umbral para obtener el primer plano.

## Región Desconocida y Marcadores:

- `cv2.connectedComponents()`: Etiqueta componentes conectados.
- `cv2.subtract()`: Calcula la región desconocida restando áreas seguras.

## Algoritmo Watershed:

- `cv2.watershed()`: Aplica el algoritmo Watershed.

## Visualización:

- `cv2.imshow()`, `cv2.waitKey()`, `cv2.destroyAllWindows()`: Para mostrar la imagen segmentada.

# Demostración de una o Varias Expresiones

### library.py

```python
import cv2
import numpy as np

def segment_watershed(image):
    assert image is not None, "La imagen no puede ser nula"
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    
    return image
```

# Llamadas a Funciones
Las funciones se llaman de manera secuencial para realizar el procesamiento de imágenes. Por ejemplo:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
```

# Asignación de Variables
Las variables se utilizan para almacenar resultados intermedios del procesamiento de imágenes:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
```
# Implementación de Flujos de Imágenes
El flujo de imágenes se maneja mediante la carga, procesamiento y visualización de imágenes. Se siguen pasos secuenciales desde la carga hasta la segmentación y visualización.

# Aplicación de Filtros de OpenCV
Se aplican varios filtros y operaciones de OpenCV, incluyendo:

- Conversión a escala de grises: cv2.cvtColor()
- Umbral binario: cv2.threshold()
- Operaciones morfológicas: cv2.morphologyEx(), cv2.dilate()
- Transformada de distancia: cv2.distanceTransform()
- Segmentación Watershed: cv2.watershed()

# Características Implementadas
- Segmentación de Imágenes: Uso del algoritmo Watershed para segmentar imágenes.
- Eliminación de Ruido: Operaciones morfológicas para limpiar la imagen.
- Visualización de Resultados: Mostrando la imagen segmentada con contornos resaltados.
- Etiquetado de Componentes Conectados: Uso de cv2.connectedComponents() para etiquetar regiones.

### translator.py
```python
# Cargar la imagen
img = cv2.imread('coins.jpeg')

# Asegurarse de que la imagen se cargue correctamente
assert img is not None, "El archivo no pudo ser leído, verifica con os.path.exists()"

# Aplicar la segmentación de Watershed
segmented_img = segment_watershed(img)

# Mostrar la imagen segmentada
cv2.imshow('Imagen Segmentada', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Ejemplo de Uso
```python
python translator.py coins.jpeg
```
> [!NOTE]
> Este comando ejecutará el script translator.py con la imagen coins.jpeg como entrada y mostrará la imagen segmentada en una ventana.

## Demostración/Resultado

<img width="250" alt="Captura de pantalla 2024-05-30 a la(s) 7 52 54 p m" src="https://github.com/ariigat0/G.I-JOE-Compiladores/assets/70560259/807853d3-acd3-4a61-baed-3a24ba0d62e7">

> [!NOTE]
> En este ejemplo, segment_watershed se importa del archivo library.py y se aplica a la imagen cargada coins.jpeg. La imagen segmentada se muestra en una ventana hasta que se presiona una tecla para cerrarla.
