# Thumbs Up/Down Detection on Jetson Nano  
This project implements a real-time gesture detection system on NVIDIA's Jetson Nano. It classifies whether a person is showing a thumbs up or thumbs down gesture, optimized for edge deployment.  


## Overview  
The system uses a lightweight convolutional neural network trained on a custom dataset of thumbs up and thumbs down gestures. It is designed to run efficiently on the Jetson Nano, leveraging its GPU capabilities for real-time inference.  


### Key Components  
- **Data Collection**: A custom dataset of gesture images collected using a standard webcam.  
- **Model Architecture**: The model is based on a lightweight CNN, with options for transfer learning using MobileNet or ResNet for improved accuracy.  
- **Training**: Includes scripts for preprocessing, model training, and evaluation.  
- **Inference**: Real-time detection pipeline optimized for the Jetson Nano's hardware capabilities.  


### Features  
- **Custom Gesture Recognition**: Detects "thumbs up" and "thumbs down" gestures with high accuracy.  
- **Edge Optimization**: Designed for real-time performance on the Jetson Nano.  
- **Scalable**: Easily adaptable to recognize additional gestures or objects.  


### Current Progress  
- Dataset creation and labeling completed.  
- Model trained with >90% accuracy on validation data.  
- Real-time detection pipeline functional and tested on live video feed.<br/><br/>  