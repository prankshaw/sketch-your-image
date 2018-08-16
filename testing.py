import numpy as np
import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imwrite("test.png",frame) # writes image test.bmp to disk

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
