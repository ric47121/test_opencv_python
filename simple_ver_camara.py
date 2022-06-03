import cv2
cam = cv2.VideoCapture(0)
# frame_width = int( cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height =int( cam.get( cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow("test")

while cam.isOpened():

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()
cv2.destroyAllWindows()