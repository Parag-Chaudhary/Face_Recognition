# Face_Recognition using One-Shot Learning

## Project Objective
To create a Face Recognition model using one-shot learning i.e, you don't have to train the model again and again for the new person you add. 

## Project Description
Here is a basic idea how face recognition works.
First of all the `Encoder.py` file takes each and every face from the datasets and then detect the face in the photo.
Then this detected face is converted into the 128-Encodings and save these encodings in a file name Encodings. This step is repeat for every photo in the datasets.
Finally the `Face_Recognition.py` file almost do same, but instead of detecting face from the photos it take the faces from the camera and then converts into 128-Encodings and instead of saving it, it compares the encodings to the saved encodings.
If the encodings are the same then person's name will pop up.

## Pre-Requisites Before running
* First of all, Please change the path of DIRECTORY in `Encoder.py` file to your working directory path.
* Install Cmake using `pip install cmake`
* Install Dlib using `pip install dlib`
* Install Face-Recognition using `pip install face_recognition OR pip install face-recognition`
* Install OpenCV using `pip install opencv-python`
* Install Pickle using `pip install pickles`

## Dataset Creation
* This is a very important step because you have to make your own Datasets as you want to recognize your or yours friend's face.
* Inside the Datasets folder their is only a Readme file.
* You have to delete this Readme file and in place of this you have to copy the photos of person' face that you want to recognize (per person per folder).
* You have to kept in mind that every photo must have only one face in it.

## Order of files to be run
* First you have to run `Encoder.py` file to create the Encodings.
* Secondly you have to run `Face_Recognition.py` file to recognize the faces.

## Result
![ezgif com-gif-maker](https://user-images.githubusercontent.com/70112406/94747341-3a21b080-039c-11eb-8edd-fcd971083852.gif)
