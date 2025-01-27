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

## Steps to Make a Virtual Enviroment
### Step 1: Create the Virtual Environment
- Navigate to your Git repository in the terminal: *cd path/to/your/git/repo*
- Create the virtual environment (e.g., venv): *python3 -m venv venv*
- This will create a venv folder inside your repository.

### Step 2: Add venv to .gitignore
- You don’t want to commit your virtual environment to Git because it can be large and system-dependent.
- Open or create a .gitignore file in the root of your repository: *nano .gitignore*
- Add the following line to ignore the virtual environment folder: *venv/*
- Save the file: *Press Ctrl + O to save, then Enter. Press Ctrl + X to exit.*
- Verify that .gitignore is working by running: *git status*
- The venv/ folder should not appear in the list of files to be staged.

### Step 3: Activate the Virtual Environment
- Activate the virtual environment whenever you’re working on the project: *source venv/bin/activate*
- Your terminal prompt will change to indicate the environment is active: *(venv) user@your-computer:~/your-repo$*

### Step 4: Install Libraries
- Install the libraries needed for your project: *pip install opencv-python tensorflow mediapipe numpy pillow matplotlib seaborn*
- Generate a requirements.txt file to track dependencies: *pip freeze > requirements.txt*
- Commit the requirements.txt file to your repository:<br/>
    *git add requirements.txt*
    *git commit -m "Add dependencies for thumbs detection"*
    *git push*

By following these steps, you can manage project dependencies efficiently and ensure a reproducible setup for collaborators. Remember to activate the virtual environment (source venv/bin/activate) every time you work on the project!