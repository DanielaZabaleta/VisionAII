#Ejercicio de clase introduccion

import cv2 as cv 
import numpy as np  

s = 100

def im_1():
    im = np.zeros([100,100])
    for i in range (s):
        im[i,i] = 255

        cv.imwrite('Imagen1.jpg', im)

im_1()

def im_2():
    im2 = np.zeros((100,100,3), np.uint8)
    rojo = cv.rectangle (im2, (35,35), (65,65), (0,0,255), -1)
    verde = cv.rectangle (rojo, (40,40), (60,60), (0,255,0), -1)
    azul = cv.rectangle (verde, (45,45), (55,55), (255,0,0), -1)
    negro = cv.rectangle (azul, (48,48), (52,52), (0,0,0), -1)

    cv.imwrite('Imagen2.jpg', negro)

im_2()

def im_3():
    im_3 = np.zeros([100,100])