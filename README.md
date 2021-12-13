# Human Counter

## Aim of Project
Canlı görüntüdeki kişileri sürekli olarak sayacak ve zaman grafiğinde gösterecek bir yazılım geliştirdim. Bazı hazır algoritmaları da bu projede kullandım. Gerekli kısımlarda açıklamalarını yazdım ve kodda da yorum satırlarında açıkladım. Bu projeyi Phyton da programladım. Görüntü alındıktan sonra oluşturulan veri ile web sayfası üzerinden kullanıcı bilgilendirildi. Kullanıcıya 30 saniyede bir veri iletilir. Kullanıcı grafikte tarihi, saati ve toplam kişi sayısına ulaşabilir.


## Yolo
YOLO v3 algorithm flow chart A convolutional neural network usually consists of an input layer, a convolutional layer, a pooling layer, and an output layer. The network inputs a two-dimensional image, and the convolution layer extracts and maps the detailed features of the image through the form of a sliding window; the pooling layer downsamples the input feature image, thereby reducing the computational complexity and extracting the main features on the one hand. The image feature information is extracted by convolving.

![YOLO](https://www.researchgate.net/publication/337451395/figure/fig2/AS:828207003602944@1574471345168/YOLO-v3-algorithm-flow-chart-A-convolutional-neural-network-usually-consists-of-an-input.jpg)

## How does YOLO work?
Prior detection systems use localizers or classifiers to carry out the detection process. Then the model is applied to an image at different scales and locations. The regions of the image with High scoring are considered for detections.

YOLO algorithm uses a completely different approach. The algorithm applies a single neural network to the entire full image. Then this network divides that image into regions which provides the bounding boxes and also predicts probabilities for each region. These generated bounding boxes are weighted by the predicted probabilities.


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


![12-12-2021 17_40_27](https://user-images.githubusercontent.com/95358360/145829827-843a498a-8bf9-4eab-8764-bfc94a78b569.jpg)


## Firebase
Google Firebase; It is a platform that allows user login authorization and data to be kept in real time and synchronously without the need for the developer to deal with the server side of web and mobile applications. With the realtime database, the necessary information reaches the user. [Times Square](https://www.youtube.com/watch?v=AdUw5RdyZxI ) bu bağlantıdaki canlı görüntüdeki kişiler sürekli olarak sayılıyor ve zaman grafiğinde gösteriliyor. 




 ![Time Square](https://user-images.githubusercontent.com/95358360/145819788-e13f3e42-3eb5-46fb-83db-4d819f5301eb.PNG)
 


# References
[To Detect the People](https://github.com/venkata-sreeram/Social-Distancing-Detection.git)

[For Firebase](https://www.youtube.com/watch?v=rKuGCQda_Qo)

[How to Configure Google Firebase for Web](https://www.youtube.com/watch?v=q5tAUb_bvqg)

[Realtime Database](https://www.w3schools.com/js/js_graphics_chartjs.asp)
