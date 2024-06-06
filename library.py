import numpy as np
import cv2
import matplotlib as plt

def load_image(path):
    path = path.strip()
    return cv2.imread(path)

def show_image(img):
    cv2.imshow('window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

def search_cv2(function_name):
    try:
        return getattr(cv2, function_name)
    except:
        pass
    return None

def get_mean(arr):
    return np.mean(arr)

def get_average(arr):
    return np.average(arr)

def get_median(arr):
    return np.median(arr)

def get_std(arr):
    return np.std(arr)

def get_histogram(arr):
    return np.histogram(arr)

def put_at(arr, idx, val):
    return np.histogram(arr, idx, val)

def gen_vector(*args):
    return np.array(args)
