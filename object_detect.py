import cv2
import mediapipe as mp

# Initialise MediaPipe Hands, which is a pre-trained model for hand landmark detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the webcam to capture frames (index 0 for the default camera)
cap = cv2.VideoCapture(0)

# Create a 'hands' object to process video frames and detect hand landmarks
with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
    
    # Loop over the frames until the webcam is closed or an error occurs
    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        # If no frame was captured, exit the loop
        if not ret:
            break
        
        # Flip the frame horizontally to create a mirror effect for a natural view
        frame = cv2.flip(frame, 1)

        # Convert the frame from BGR (default in OpenCV) to RGB (used by MediaPipe)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the RGB frame to detect hands and hand landmarks
        result = hands.process(rgb_frame)

        # If any hand landmarks are detected, proceed with further processing
        if result.multi_hand_landmarks:
            # Loop over the detected hands (in case multiple hands are detected)
            for hand_landmarks in result.multi_hand_landmarks:
                
                # Draw the landmarks and connections on the frame (skeleton of the hand)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Retrieve specific hand landmarks for gesture detection
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
                index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                
                # Analyze the relative positions of the thumb and index finger to detect the gesture
                # Thumbs Up: thumb tip and thumb IP (Intermediate Phalanx) are above the MCP of the index finger
                if thumb_tip.y < index_mcp.y and thumb_ip.y < index_mcp.y:
                    gesture = "Thumbs Up"
                # Thumbs Down: thumb tip and thumb IP are below the MCP of the index finger
                elif thumb_tip.y > index_mcp.y and thumb_ip.y > index_mcp.y:
                    gesture = "Thumbs Down"
                # Neutral position if thumb is neither fully up nor down
                else:
                    gesture = "Neutral"

                # Display the detected gesture (Thumbs Up/Down/Neutral) on the frame
                cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame with landmarks and the gesture detected
        cv2.imshow("Thumbs Detector", frame)
        
        # Exit the loop when the 'Esc' key (key code 27) is pressed
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the webcam and close all OpenCV windows after the loop ends
cap.release()
cv2.destroyAllWindows()