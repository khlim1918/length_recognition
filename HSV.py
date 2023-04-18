import cv2

src = cv2.imread('before.jpg', cv2.IMREAD_COLOR
src = cv2.pyrDown(src)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBar Windows")
cv2.createTrackbar("H-Low1", "TrackBar Windows", 0, 180, lambda x: x)
cv2.createTrackbar("H-High1", "TrackBar Windows", 0, 180, lambda x: x)
cv2.createTrackbar("H-Low2", "TrackBar Windows", 0, 180, lambda x: x)
cv2.createTrackbar("H-High2", "TrackBar Windows", 0, 180, lambda x: x)
cv2.createTrackbar("S-Th", "TrackBar Windows", 0, 255, lambda x: x)
cv2.createTrackbar("V-Th", "TrackBar Windows", 0, 255, lambda x: x)
cv2.setTrackbarPos("H-Low1", "TrackBar Windows", 0)
cv2.setTrackbarPos("H-High1", "TrackBar Windows", 5)
cv2.setTrackbarPos("H-Low2", "TrackBar Windows", 170)
cv2.setTrackbarPos("H-High2", "TrackBar Windows", 180)
cv2.setTrackbarPos("S-Th", "TrackBar Windows", 100)
cv2.setTrackbarPos("V-Th", "TrackBar Windows", 100)

while cv2.waitKey(1) != ord('q'):
    hsv1_low = cv2.getTrackbarPos("H-Low1", "TrackBar Windows")
    hsv1_high = cv2.getTrackbarPos("H-High1", "TrackBar Windows")
    hsv2_low = cv2.getTrackbarPos("H-Low2", "TrackBar Windows")
    hsv2_high = cv2.getTrackbarPos("H-High2", "TrackBar Windows")
    hsv_s = cv2.getTrackbarPos("S-Th", "TrackBar Windows")
    hsv_v = cv2.getTrackbarPos("V-Th", "TrackBar Windows")
    lower_hsv = cv2.inRange(hsv, (hsv1_low, hsv_s, hsv_v), (hsv1_high, 255, 255))
    upper_hsv = cv2.inRange(hsv, (hsv2_low, hsv_s, hsv_v), (hsv2_high, 255, 255))
    added_hsv = cv2.addWeighted(lower_hsv, 1.0, upper_hsv, 1.0, 0.0)
    hsv_out = cv2.bitwise_and(hsv, hsv, mask=added_hsv)
    result = cv2.cvtColor(hsv_out, cv2.COLOR_HSV2BGR)
    cv2.imshow("TrackBar Windows", result)