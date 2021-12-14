# Human Counter

## Aim of Project
In this project, I developed an algorithm that will count the people in the live view continuously and display them on the time graph. I also used and developed some algorithms as a reference in this project. I wrote this project in Python and used the OpenCV library. I used Python to send data to the database. I used javascript to pull the data. After processing the image as a result of various algorithms, the user was informed via the web page with the data generated in real-time. Data is transmitted to the user every 30 seconds. The user can access the date, time, and total number of people on the graph.


## YOLO
YOLO is an algorithm for object detection using convolutional neural networks. When the YOLO algorithm starts working, it detects objects in images or videos and their coordinates at the same time.
The only difference between video and image processing is that images consist of a single frame, while videos consist of many frames. The algorithm works for a single frame in images, while in videos it works repeatedly for all frames. 

## Working Principle of YOLO Algorithm
YOLO algorithm first divides the image into regions. It then draws the bounding boxes surrounding the objects in each region and calculates the probability of finding an object in each region.

It also calculates a confidence score for each bounding box. This score tells us with what percent probability the object is the predicted object. A technique called non-maximum suppression is applied to the objects inside the bounding boxes. This technique excludes objects with a lower confidence score from evaluation and checks for the presence of a higher confidence bounding box in the same region.
  
  ![frame2](https://user-images.githubusercontent.com/95358360/145855221-e3e4186e-fd7f-47b6-b65f-3747e5d5e5a8.PNG)
  
It is investigated whether there are objects in each region. If an object is found, its midpoint, height, and width are found. Then the bounding box is drawn. Many sub-processes must be performed for this. A prediction vector is generated for each region. These vectors include the confidence score.

If the confidence score is 0, there is no object there, and if it is 1, there is an object there. More than one bounding box can be drawn for the same object within the same. Non-maximum suppression technique is used to get rid of this problem. The aim is, what is done with this technique is simply that the bounding box with the highest confidence score stays and the others are removed from the view. After all operations, the following output is accessed:
  
 
 ![frame3](https://user-images.githubusercontent.com/95358360/145855367-61c8c461-17ab-45e2-bd1a-fd482b8ae107.PNG)

## yolov3.weights

Download official yolov3.weights and put it on top floder of project.


[yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)

### Colab between Drive Mount

Colaboratory, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser and is especially well suited to machine learning, data analysis, and education. Operating system; It is a set of software that manages hardware resources running on the computer and provides common services for various application software. First of all, I used my operating system, but it was insufficient. Because my processor was not good, I ran this project on Colab. I pulled the files from Drive to Colab. This both kept my files safe and I wanted to use this feature of Colab. I also made this link with the code block below.


```
#code block
from google.colab import drive
drive.mount('/content/gdrive')
%cd ./gdrive
%cd ./MyDrive/task-1 
```

## Output


![frame7](https://user-images.githubusercontent.com/95358360/145902992-34279b27-6aa2-4b84-ae72-de4c5ecfee22.PNG)




## Firebase

The total number of people and the current time are sent to the real-time database on firebase every 30 seconds. Then, every 30 seconds, the number of people and time data are taken from the real-time database in firebase. It is then graphically displayed on the website.
I used Google Firebase for the database. Google Firebase; is a platform that allows user login authorization and data to be kept in real-time and synchronously without the need for the developer to deal with the server-side of web and mobile applications. With the real-time database, the necessary information reaches the user. People in live view in this link [Times Square](https://www.youtube.com/watch?v=AdUw5RdyZxI ) are counted continuously and displayed on a time graph.





![frame5](https://user-images.githubusercontent.com/95358360/145856859-bda12886-4c7c-45f9-93ac-6e9375c9c35d.PNG)
 


# References
[To Detect the People](https://github.com/venkata-sreeram/Social-Distancing-Detection.git)

[For Firebase](https://www.youtube.com/watch?v=rKuGCQda_Qo)

[How to Configure Google Firebase for Web](https://www.youtube.com/watch?v=q5tAUb_bvqg)

[Realtime Database](https://www.w3schools.com/js/js_graphics_chartjs.asp)
