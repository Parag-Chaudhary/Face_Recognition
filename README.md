# Face_Recognition using One-Shot Learning

## Project Objective
To create a Face Recognition model using one-shot learning i.e, you don't have to train the model again and again for the new person you add. 

## Project Description
Here is a basic idea how face recognition works.
First of all the Encoder.py file takes each and every face from the datasets and then detect the face in the photo.
Then this detected face is converted into the 128-Encodings and save these encodings in a file name Encodings. This step is repeat for every photo in the datasets.
Finally the Face_Recognition.py file almost do same, but instead of detecting face from the photos it take the faces from the camera and then converts into 128-Encodings and instead of saving it, it compares the encodings to the saved encodings.
If the encodings are the same then person's name will pop up.

## Pre-Requisites Before running
* First of all, Please change the path of DIRECTORY in Encoder.py file to your working directory path.
* Install Cmake using pip install cmake.
* Install Dlib using pip install dlib.
* Install Face-Recognition using pip install face_recognition
* Install OpenCV using pip install opencv-python
* Install Pickle using pip install pickles

## Dataset Creation
