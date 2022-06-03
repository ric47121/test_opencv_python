import cv2
cam = cv2.VideoCapture(0)
frame_width = int( cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cam.get( cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow("test")

# https://noemioocc.github.io/posts/VideoWriter-openCV-python/
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# <VideoWriter object> = cv2.VideoWriter(filename, fourcc, fps, frameSize)
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (frame_width,frame_height))

while cam.isOpened():

    ret, frame = cam.read()
    out.write(frame)

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