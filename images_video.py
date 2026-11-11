import cv2 as cv

img = cv.imread(r'pics\20261106_180431.jpg')
# cv.imshow('image', img)


def reshaping(frame, scale=0.30):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dims = (width, height)
    
    return cv.resize(frame,dims, interpolation=cv.INTER_AREA)

res = reshaping(img)

capture = cv.VideoCapture(r"\images\ee4f6a60889b4defb8285d5d69c2b01b.mp4")

while True:
    isTrue, frame = capture.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    dilate = cv.dilate(gray, (7, 7), iterations=3)
    canny = cv.Canny(gray, 18,18)   
    blured = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    
    cv.imshow('Canny', canny)
    cv.imshow('Dilated', dilate)
    cv.imshow('Grayed', gray)
    cv.imshow('Video', canny)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    

capture.release()
cv.destroyAllWindows()
