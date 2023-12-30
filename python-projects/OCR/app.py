import cv2 as cv
import pytesseract as tes
img = cv.imread('demo.jpg')

height,width,_ = img.shape
roi = img[50:500, 200:600]

print(tes.image_to_string(roi))

cv.imshow('roi',roi)
cv.waitKey(0)
cv.destroyAllWindows()
