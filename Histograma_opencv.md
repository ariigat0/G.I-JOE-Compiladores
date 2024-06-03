# Implementación de visualización de histogramas con opencv
## Reglas de la gramática implementada

La gramática que se puede inferir del código proporcionado para el análisis y manipulación de imágenes se puede describir a través de un conjunto de reglas que dictan cómo deben ser estructuradas las funciones y las operaciones que realizan. Aquí están las reglas de la gramática implementada:

## 1. Importación de Bibliotecas

```python
import numpy as np
import cv2
import matplotlib.pyplot as plt
```

## 2. Definición de Funciones

Cada función debe comenzar con la palabra clave def seguida del nombre de la función y paréntesis que pueden contener parámetros. La función debe terminar con dos puntos : y contener un bloque de código indentado.

```python
def function_name(parameters):
```

## 3. Funciones para Manipulación de Imágenes
> [!NOTE]
> _load_image(path)_: Recibe un path (cadena de texto) que especifica la ruta de la imagen, la lee usando cv2.imread y devuelve la imagen como una matriz.

```python
def load_image(path):
    path = path.strip()
    return cv2.imread(path)
```
> [!NOTE]
> _show_image(img)_: Recibe una imagen (img) y la muestra en una ventana utilizando cv2.imshow. La función espera una tecla para cerrar la ventana.

```python
def show_image(img):
    cv2.imshow('foquita', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
```
> [!NOTE]
>_search_cv2(function_name)_: Recibe un nombre de función (function_name) como cadena y trata de devolver la función correspondiente del módulo cv2 usando getattr.

```python
def search_cv2(function_name):
    try:
        return getattr(cv2, function_name)
    except AttributeError:
        pass
    return None
```

> [!NOTE]
> _gen_vector(*args)_: Recibe un número variable de argumentos y devuelve un vector (array de Numpy) con esos argumentos.

```python
def gen_vector(*args):
    return np.array(args)
```

## 4. Generación de Histogramas

> [!NOTE]
>_ show_histograma(image)_: Recibe una imagen, verifica que no sea None, crea una máscara, calcula los histogramas con y sin máscara y muestra las imágenes y los histogramas utilizando matplotlib.pyplot.

```python
def show_histograma(image):
    assert image is not None, "La imagen no puede ser nula"

# Crear una máscara
    mask = np.zeros(image.shape[:2], np.uint8)
    mask[100:300, 100:400] = 255
    masked_img = cv2.bitwise_and(image, image, mask=mask)
    
    # Calcular histogramas con y sin máscara
    hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])
    
    # Mostrar las imágenes y los histogramas
    plt.subplot(221), plt.imshow(image, 'gray')
    plt.title('Imagen Original')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.title('Máscara')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.title('Imagen con Máscara')
    plt.subplot(224), plt.plot(hist_full, label='Histograma Completo')
    plt.plot(hist_mask, label='Histograma con Máscara')
    plt.xlim([0, 256])
    plt.legend()
    plt.title('Histogramas')
    
    plt.show()
```

    
  
### Ejemplo de Uso
```python
img = load_image('foquita.jpg')
show_histograma(img)
```
### Demostración/Resultado

<img width="643" alt="Captura de pantalla 2024-05-30 a la(s) 6 19 19 p m" src="https://github.com/ariigat0/G.I-JOE-Compiladores/assets/70560259/37fab615-d51a-46bb-8452-339b5cafd10d">



