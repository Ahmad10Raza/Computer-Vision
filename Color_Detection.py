import cv2
import numpy as np

# Create a video capture object for the default camera (0)
cap = cv2.VideoCapture(0)

# Callback function for trackbar adjustments (does nothing)
def nothing(x):
    pass

# Create a window for adjusting color parameters
cv2.namedWindow("Color Adjustments")

# Create trackbars to adjust lower and upper HSV values for color detection
cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)

while True:
    # Read a frame from the video capture
    _, frame = cap.read()
    
    # Resize the frame for better display (optional)
    frame = cv2.resize(frame, (400, 400))

    # Convert the BGR frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the current trackbar positions for lower and upper HSV values
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")
    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")
    
    # Create lower and upper bounds for the specified color range
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    # Create a mask based on the color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Apply the mask to the original frame to extract the specified color
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, the mask, and the color-extracted result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Masking", mask)
    cv2.imshow("Result", res)

    # Wait for a key press and break the loop if the 'Esc' key is pressed
    key = cv2.waitKey(25) & 0xFF
    if key == 27:
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
