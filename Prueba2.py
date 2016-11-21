import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("1.jpg", 0)
"""hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(121),plt.imshow(img,"gray")
plt.subplot(122),plt.plot(hist)
plt.xlim([0,256])
plt.show()"""

ret, binario = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagen - Binarios", binario)
# print("retval: " + str(ret))

kernel = np.ones((6, 6), np.uint8)
erosion = cv2.erode(binario, kernel)
cv2.imshow("erosion", erosion)

dilatacion = cv2.dilate(erosion, kernel, iterations=2)
cv2.imshow("dilatacion", dilatacion)

_, contorno, _ = cv2.findContours(image=erosion, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, contorno, -1, (0, 255, 0), 2)
cv2.imshow("Imagen - Contorno", img)

count_5cents = {"cantidad": 0, "total": 0}
count_10cents = {"cantidad": 0, "total": 0}

for cont in contorno:
    cont = cv2.contourArea(cont)
    if cont > 1800:
        count_5cents["cantidad"] += 1
        count_5cents["total"] += 5
    elif cont < 1700:
        count_10cents["cantidad"] += 1
        count_10cents["total"] += 10


print("Total de Dinero: ", count_10cents["total"] + count_5cents["total"], "centavos")
print("Total de Monedas: ", count_10cents["cantidad"] + count_5cents["cantidad"], "monedas")
print("Total de Monedas de 5 centavos: ", count_5cents["cantidad"])
print("Total de Monedas de 10 centavos: ", count_10cents["cantidad"])


"""
cv2.imshow('ventana', img)


print img.shape
print img.size
print img.dtype
"""

cv2.waitKey(0)
