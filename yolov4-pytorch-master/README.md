

## 目录
1. [Performance of Yolo v4 compared with other algorithms on VOC dataset]
2. [Bonet, modified_Bonet, add_Bonet]
3. [Performance of our method]
4. [performance on differernt dataset]


## 1. Performance of Yolo v4 compared with other algorithms on VOC dataset
For two-dimensional object detection algorithms, we firstly compare Yolo v4 algorithms with other object detection algorithms such as SSD and Retinanet.
![image](https://user-images.githubusercontent.com/59796732/133000842-24d57585-f6da-48e2-b5cb-b06feee29fe4.png)
The picture of object detection 
![捕获](https://user-images.githubusercontent.com/59796732/133000943-c89a129e-0c4c-4cf0-ba1b-3dede6125abe.PNG)
![image](https://user-images.githubusercontent.com/59796732/133000986-75781631-4718-469b-a70e-8429782604d7.png)
The comparsion between SSD, Yolo v4 and Retinanet
Conclusion: We found that while Yolo v4 was significantly less mAP than SSD and Retinanet in initial training, yolo v4 was eventually higher than the latter two, and yolo v4's FPS was much higher than SSD and Retinanet, proving that its accuracy and speed performance were good. Therefore, we intend to further study Yolo and try to change its principal network structure to improve the accuracy rate.

## 2. Bonet, modified_Bonet and add_Bonet
With the development of convolutional neural networks, Tsung-Yi Lin et al. have found that because the characteristics of small targets are easily lost in convolution, the detection results of small targets of most convolutional neural networks are poor. Tsung-Yi Lin and others then proposed feature pyramid methods(FPN) for object detection tasks to solve this problem. The essence of this method is to make the two-upsample in this process, and then concatenate the higher feature map with the lower-level feature map, and then process the convolution process. With the appearance of FPN, many other methods including Panet has been put forward. Thus, we aim to create new method in the basis of Panet. 
![image](https://user-images.githubusercontent.com/59796732/133001130-93b31e8b-5fa9-49df-934b-25fbde2d7487.png)
Therefore, based on other people's findings, we speculate that as feature pyramids become more complex, model accuracy will improve. We intend to further complicate the feature pyramid on the basis of Panet, and we intend to design two convolution networks to compensate for the current Panet deficiencies. First of all, there is no way to consider the network degradation in the two-dimensional target detection algorithm, and we think that CSPDarknet53 network already has a certain depth, so we want to use the idea of residual network to prevent network degradation in the process of feature pyramid. 
![cancha](https://user-images.githubusercontent.com/59796732/133001676-2bd0f379-5dc2-451f-8448-8237a4aca209.png)
Normal thought on the residual connection
In addition, most feature pyramids are using concatenation method for feature fusion. Therefore, we intend to concatenate the information of the original feature x map into the feature map after two convolutions (that is conv(conv(x))), so as to draw on the residual connection idea and retain the way the feature pyramids are concatenated:
![image](https://user-images.githubusercontent.com/59796732/133001693-54c3e94b-d6ad-470f-9061-cd98ce393871.png)
Original Panet Structure: 
![panet](https://user-images.githubusercontent.com/59796732/133001808-4640fad1-8f04-4f04-9c97-ee7e896fb04d.png)
Our thought on the structure of The residual connection:
![Bonet](https://user-images.githubusercontent.com/59796732/133001796-db513df3-5c99-4dbe-9f8c-75627b1905af.png)
In addition, we try to complexize the network by adding one step of upsampling and downsampling and we call it modified-bonet:
![modified _bonet](https://user-images.githubusercontent.com/59796732/133001937-d26a7ccf-da29-402d-9be4-6f91eee3630c.png)

Finally, We totally change the method from concatenation into addition and call it add_bonet:
![add_bonet](https://user-images.githubusercontent.com/59796732/133001911-01cc04c5-876e-4f87-8911-2f2e4498090b.png)


## 3. Performance of our method 















