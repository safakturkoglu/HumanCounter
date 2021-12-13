# Human Counter

## Aim of Project
In this project, I developed an algorithm that will count the people in the live view continuously and display them on the time graph. I also used and developed some algorithms as a reference in this project. I wrote this project in Python and used the OpenCV library. After processing the image as a result of various algorithms, the user was informed via the web page with the data generated in real time. Data is transmitted to the user every 30 seconds. The user can access the date, time and total number of people on the chart.


## YOLO
YOLO is an algorithm for object detection using convolutional neural networks. When the YOLO algorithm starts working, it detects objects in images or videos and their coordinates at the same time.
The only difference between video and image processing is that images consist of a single frame, while videos consist of many frames. The algorithm works for a single frame in images, while in videos it works repeatedly for all frames. 

## Working Principle of YOLO Algorithm
YOLO algorithm first divides the image into regions. It then draws the bounding boxes surrounding the objects in each region and calculates the probability of finding an object in each region.

It also calculates a confidence score for each bounding box. This score tells us with what percent probability the object is the predicted object. A technique called non-maximum suppression is applied to the objects inside the bounding boxes. This technique excludes objects with a lower confidence score from evaluation and checks for the presence of a higher confidence bounding box in the same region.
  
  ![frame2](https://user-images.githubusercontent.com/95358360/145855221-e3e4186e-fd7f-47b6-b65f-3747e5d5e5a8.PNG)
  
  Her bir bölgede nesne olup olmadığı araştırılır. Eğer bir nesne bulunursa o nesnenin orta noktası, yüksekliği ve genişliği bulunur. Daha sonra bounding box çizilir. Bunun yapılabilmesi için bir takım alt işlemlerin yapılması gerekir. Her bir bölge için bir tahmin vektörü oluşturulur. Bu vektörlerin içinde güven skoru yer alır. 

Eğer güven skoru 0 ise orada nesne yok, 1 ise orada nesne var demektir. Aynı içerisindeki aynı nesne için birden fazla bounding box çizdirilebilir. Bu sorundan kurtulmak için non-maximum suppression tekniği kullanılır. Bu teknik ile yapılan şey basitçe, en yüksek güven skoru olan bounding box’ın kalması diğerlerinin ise görüntüden atılmasıdır. Tüm işlemlerden sonra aşağıdaki çıktıya erişilir:
  
 
 ![frame3](https://user-images.githubusercontent.com/95358360/145855367-61c8c461-17ab-45e2-bd1a-fd482b8ae107.PNG)


### Colab between Drive Mount

Colaboratory, or “**Colab**” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education. 
Operating system; It is a set of software that manages hardware resources running on the computer and provides common services for various application software. First of all, I used my own operating system, but it was insufficient. Because my processor was not good, I ran this project on Colab. I pulled the files from Drive to Colab. This both kept my files safe and I wanted to use this feature of Colab. I also made this link with the code block below.


```
#code block
from google.colab import drive
drive.mount('/content/gdrive')
%cd ./gdrive
%cd ./MyDrive/task-1 
```

## Output


![frame4](https://user-images.githubusercontent.com/95358360/145856514-812fe7e8-9e72-4fef-b832-dc637542e6e0.PNG)



## Firebase
Google Firebase; It is a platform that allows user login authorization and data to be kept in real time and synchronously without the need for the developer to deal with the server side of web and mobile applications. With the realtime database, the necessary information reaches the user. [Times Square](https://www.youtube.com/watch?v=AdUw5RdyZxI ) bu bağlantıdaki canlı görüntüdeki kişiler sürekli olarak sayılıyor ve zaman grafiğinde gösteriliyor. 



![frame5](https://user-images.githubusercontent.com/95358360/145856859-bda12886-4c7c-45f9-93ac-6e9375c9c35d.PNG)
 


# References
[To Detect the People](https://github.com/venkata-sreeram/Social-Distancing-Detection.git)

[For Firebase](https://www.youtube.com/watch?v=rKuGCQda_Qo)

[How to Configure Google Firebase for Web](https://www.youtube.com/watch?v=q5tAUb_bvqg)

[Realtime Database](https://www.w3schools.com/js/js_graphics_chartjs.asp)
