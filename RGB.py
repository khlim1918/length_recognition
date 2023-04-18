import cv2

# trackbar function
def nothing(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)

#input image
img_color = cv2.imread('before.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary", img_binary)

    #esc 누르면 탈출
    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.destroyAllWindows()


"""
#seperate black area
lower_black = (0, 0, 0)
upper_black = (100, 50, 30)

img_black = cv2.inRange(img_color, lower_black, upper_black)

cv2.imshow('img_black', img_black)
cv2.waitKey(0)
cv2.destroyAllWindows()


#seperate brown area
lower_brown = (100, 50, 80)
upper_brown = (200, 150, 180)

img_brown = cv2.inRange(img_color, lower_brown, upper_brown)

cv2.imshow('img_brown', img_brown)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
