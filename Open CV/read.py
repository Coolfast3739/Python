import cv2 as cv 
capture = cv.VideoCapture('IMG_1422.MOV')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


cv.waitKey(0)
capture.release()
cv.destroyAllWindows()