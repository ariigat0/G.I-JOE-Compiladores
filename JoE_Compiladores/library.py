import numpy as np
import cv2
import matplotlib.pyplot as plt


def load_image(path):
   path = path.strip()
   return cv2.imread(path) # regresa una matriz
  


def show_image(img):
   cv2.imshow('foquita', img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   return img


def search_cv2(function_name):
   try:
       return getattr(cv2, function_name)
   except:
       pass
   return None


def gen_vector(*args):
   return np.array(args)

# Histograma
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

# Segmentacion con Watershed 
def segment_watershed(image):
    assert image is not None, "La imagen no puede ser nula"
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un umbral binario inverso con Otsu
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Eliminación de ruido
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Área segura de fondo
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    
    # Encontrar área segura de primer plano
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    # Encontrar región desconocida
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Etiquetado de marcadores
    ret, markers = cv2.connectedComponents(sure_fg)
    
    # Añadir uno a todas las etiquetas para que el fondo seguro no sea 0, sino 1
    markers = markers + 1
    
    # Marcar la región desconocida con cero
    markers[unknown == 255] = 0
    
    # Aplicar el algoritmo de Watershed
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    
    return image

# Ejemplo de uso
img = cv2.imread('coins.jpeg')
segmented_img = segment_watershed(img)

# Mostrar la imagen segmentada
cv2.imshow('Imagen Segmentada', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
