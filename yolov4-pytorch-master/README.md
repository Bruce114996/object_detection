

## 目录
1. [Performance of Yolo v4 compared with other algorithms on VOC dataset]
2. [Bonet, modified_Bonet, add_Bonet]
3. [Performance of our method]
4. [performance on differernt dataset]


## 1. [Performance of Yolo v4 compared with other algorithms on VOC dataset]
For two-dimensional object detection algorithms, we firstly compare Yolo v4 algorithms with other object detection algorithms such as SSD and Retinanet.

The picture of object detection:

![image](https://user-images.githubusercontent.com/59796732/133000842-24d57585-f6da-48e2-b5cb-b06feee29fe4.png)

The comparsion between SSD, Yolo v4 and Retinanet:
![捕获](https://user-images.githubusercontent.com/59796732/133001974-ad519817-9a6c-4174-857b-8dac5515bb47.PNG)


Conclusion: We found that while Yolo v4 was significantly less mAP than SSD and Retinanet in initial training, yolo v4 was eventually higher than the latter two, and yolo v4's FPS was much higher than SSD and Retinanet, proving that its accuracy and speed performance were good. Therefore, we intend to further study Yolo and try to change its principal network structure to improve the accuracy rate.

## 2. [Bonet, modified_Bonet and add_Bonet]
With the development of convolutional neural networks, Tsung-Yi Lin et al. have found that because the characteristics of small targets are easily lost in convolution, the detection results of small targets of most convolutional neural networks are poor. Tsung-Yi Lin and others then proposed feature pyramid methods(FPN) for object detection tasks to solve this problem. The essence of this method is to make the two-upsample in this process, and then concatenate the higher feature map with the lower-level feature map, and then process the convolution process. With the appearance of FPN, many other methods including Panet has been put forward. Thus, we aim to create new method in the basis of Panet.

![image](https://user-images.githubusercontent.com/59796732/133001130-93b31e8b-5fa9-49df-934b-25fbde2d7487.png)

Therefore, based on other people's findings, we speculate that as feature pyramids become more complex, model accuracy will improve. We intend to further complicate the feature pyramid on the basis of Panet, and we intend to design two convolution networks to compensate for the current Panet deficiencies. First of all, there is no way to consider the network degradation in the two-dimensional target detection algorithm, and we think that CSPDarknet53 network already has a certain depth, so we want to use the idea of residual network to prevent network degradation in the process of feature pyramid. 
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


## 3. [Performance of our method] 

![捕获2](https://user-images.githubusercontent.com/59796732/133002138-2fbc1507-e834-49d7-a4f0-cf72ddf085bf.PNG)

From the table above, we learn that the Add-Bonet method performs much better in the VOC dataset than the Bonet method, so we think that changing the way features are fused will improve the accuracy of detection. For speed, we found that the Add-Bonet methods using the couple mechanism detect faster than other feature pyramid methods that use stacking.

## 4. [performance on differernt dataset]
Besides the traditional VOC dataset, we apply our method on other dataset. Firstly, we have made the photograph on campus, but the accuracy does not show well as the limitation of our electronics. Secondly, we seek for the professional traffic dataset: DETRAC which consists of 10 thousands of training data. 

The Effect of our method on the two datasets:

![image](https://user-images.githubusercontent.com/59796732/133002208-ce9cc78a-4f3c-4fff-9348-906eb7391f9c.png)

The performance of our method on two datasets:

![捕获3](https://user-images.githubusercontent.com/59796732/133002361-18e71601-2a53-4f94-ace4-fa0effd94306.PNG)

From the results, we can learn that Bonet and Modified-Bonet was more accurate than Panet in the traffic dataset, which proves that the residual structure we proposed to include residual structures in the feature pyramid is suitable for some datasets and that different convolution networks may behave very differently on different datasets. On the other hand, we further propose the add-Bonet methods that increase the accuracy by about 2% and 0.5 FPS on the basis of the original Yolo v4.















