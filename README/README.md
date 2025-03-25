# Face and Smile Detection using OpenCV
## Overview
This project is a real-time face and smile detection application built with Python and OpenCV. It leverages Haar cascade classifiers to detect faces and smiles in a video feed, distinguishing them visually with color-coded rectangles. The program runs on devices like the Jetson Nano, making it an excellent introduction to computer vision and real-time image processing.

## Key Components
- **Haar Cascade Classifiers:** Pre-trained models for face (haarcascade_frontalface_default.xml) and smile detection (haarcascade_smile.xml).
- **OpenCV Library:** Used for video capture, grayscale conversion, and real-time feature detection.
- **Jetson Nano Compatibility:** Optimized for lightweight hardware, suitable for testing computer vision algorithms.

## Features
- **Real-Time Detection:** Detects faces and smiles in a live video feed.
- **Color-Coded Visualization:** Blue rectangles for faces. Green rectangles for smiles.
- **Customizable Detection Parameters:** Adjust sensitivity and accuracy for different environments by modifying scaleFactor, minNeighbors, and minSize.
- **Simple Controls:** Press q to quit the application.

## Network Transmission
- Some simple code to transmit data from the Jetson Nano to a local machine on the same network.
