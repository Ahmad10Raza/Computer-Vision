import cv2
import numpy as np

# Create a video capture object for the default camera (0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles using the Hough Circle Transform
    circles = cv2.HoughCircles(
        gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=250, param2=30, minRadius=0, maxRadius=0
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            # Draw the circle on the original frame
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Display the frame with detected circles
    cv2.imshow("Circle Detection", frame)

    # Exit the loop if the 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
