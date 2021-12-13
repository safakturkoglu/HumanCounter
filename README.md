# Human Counter

## Aim of Project
Bu projede canlı görüntüdeki kişileri sürekli olarak sayacak ve zaman grafiğinde gösterecek bir algoritma geliştirdim. Bazı algoritmaları da bu projede referans olarak kullandım. Bu projeyi Phyton dilinde yazdım ve OpenCV kütüphanesini kullandım. Çeşitli algoritmalar sonucunda görüntü işlendikten sonra gerçek zamanlı oluşturulan veri ile web sayfası üzerinden kullanıcı bilgilendirildi. Kullanıcıya 30 saniyede bir veri iletilir. Kullanıcı grafikte tarihi, saati ve toplam kişi sayısına ulaşabilir.


## Yolo
 YOLO, konvolüsyonel sinir ağlarını kullanarak nesne tespiti yapan bir algoritmadır. YOLO algoritması çalışmaya başladığında görüntülerdeki veya videolardaki nesneleri ve bu nesnelerin koordinatlarını aynı anda tespit eder. 
Video ve resim işleme arasında tek fark resimlerin tek bir kareden (frame), videoların ise birçok kareden oluşmasıdır. Resimlerde algoritma tek bir kare için çalışırken, videolarda tüm kareler için tekrar tekrar çalışır.  

## Working Principle of YOLO Algorithm
YOLO algoritması, öncelikle görüntüyü bölgelere ayırır. Daha sonra her bir bölgedeki nesneleri çevreleyen kutuları (bounding box) çizer ve her bir bölgede nesne bulunma olasılığı ile ilgili bir hesabı yapar.

Ayrıca her bir bounding box için bir güven skoru hesaplar. Bu skor bize o nesnenin yüzde kaç olasılıkla tahmin edilen nesne olduğunu söyler. Örneğin, bulunan bir araba için güven skoru 0,3 ise bunun anlamı o nesnenin araba olma olasığının oldukça düşük olduğudur. Diğer bir deyişle, YOLO yaptığı tahminin güvenilmez olduğunu bize söyler.  Bounding box’ların içindeki nesnelere non-maximum suppression denen bir teknik uygulanır. Bu teknik güven skoru düşük olan nesneleri değerlendirmeden çıkarır ve aynı bölgede güven skoru daha yüksek bir bounding box‘ın varlığını kontrol eder.
  
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
