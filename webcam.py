import cv2

# Open a connection to the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

def rescaleFrame(frame, scale = 0.75): 
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Video Capture", rescaleFrame(frame, 0.4))

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
