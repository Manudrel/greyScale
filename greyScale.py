import cv2

img = cv2.imread('gatito.jpg') # Nome do arquivo de imagem
cv2.imshow('Imagem Original', img)


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem em Cinza', gray_img)

_, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Imagem Binarizada', binary_img)

cv2.waitKey(0)
cv2.destroyAllWindows()