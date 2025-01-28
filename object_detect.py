import cv2

# Load Haar cascades for face and smile detection
# These are pre-trained XML models included with OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Start video capture from the default camera (usually webcam)
cap = cv2.VideoCapture(0)

# Set the camera to capture at a lower frame rate (15 FPS) to reduce processing load
cap.set(cv2.CAP_PROP_FPS, 15)

# Initialise a frame counter to track which frame is being processed
frame_count = 0

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        # If no frame is captured, break the loop (e.g., camera disconnected)
        break

    # Resize the frame to 640x480 for faster processing
    # Lower resolution reduces the number of pixels processed by the algorithm
    frame_resized = cv2.resize(frame, (640, 480))

    # Convert the frame to grayscale as Haar cascades work with grayscale images
    gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Perform face detection only on every 5th frame to reduce CPU usage
    if frame_count % 5 == 0:
        # Detect faces in the grayscale frame
        # scaleFactor: Determines the reduction in size for each image scale
        # minNeighbors: Specifies how many neighbors each rectangle candidate should have to retain it
        # minSize: Minimum possible object size (to ignore small detections)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    else:
        # Skip detection on other frames to save computation time
        faces = []

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Draw a blue rectangle around the detected face
        # Rectangle is drawn on the resized frame to visually represent detection
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Define the region of interest (ROI) within the detected face for smile detection
        # Restricting smile detection to the face area saves computational resources
        roi_gray = gray_frame[y:y + h, x:x + w]  # Grayscale ROI for smile detection
        roi_color = frame_resized[y:y + h, x:x + w]  # Color ROI for displaying rectangles

        # Detect smiles in the ROI using the smile cascade
        # scaleFactor: Adjusted for finer scale reduction
        # minNeighbors: Higher value reduces false positives
        # minSize: Minimum size for detected smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))

        # Loop through all detected smiles in the ROI
        for (sx, sy, sw, sh) in smiles:
            # Draw a green rectangle around the detected smile
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    # Display the processed frame with rectangles drawn around detected faces and smiles
    cv2.imshow("Face and Smile Detection", frame_resized)

    # Increment the frame counter for tracking which frames to process
    frame_count += 1

    # Break the loop if the 'q' key is pressed
    # cv2.waitKey() captures key presses, and 1 ms delay allows real-time display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()