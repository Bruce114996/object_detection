## 1. Complex Yolo v4 vs Yolo v4
The PyTorch Implementation based on YOLOv4 of the paper: [Complex-YOLO: Real-time 3D Object Detection on Point Clouds](https://arxiv.org/pdf/1803.06199.pdf)
The accuracy of Yolo v4 and Complex Yolo v4:
![捕获](https://user-images.githubusercontent.com/59796732/133002872-f82bf680-253f-49cf-b60d-1b1ba802d1c9.PNG)

The Effect of Yolo v4(Two-dimensional object detection method) vs Complex Yolo v4(Three-dimsensional object detection method)
![image](https://user-images.githubusercontent.com/59796732/133002908-7e0fa2f7-4723-49fd-9d18-a8e708b8180e.png)

## 2. Complex Yolo v4 vs other three-dimensional object detection method 
![捕获4](https://user-images.githubusercontent.com/59796732/133002968-bcfe55dc-f540-4a94-be3a-bd7124aa71eb.PNG)

From the result above, Although the accuracy of The Complex Yolo v2 is not as high as that of other object detection methods, with the continuous improvement of the Yolo series network structure, the final accuracy is much greater than other methods. Therefore, it is feasible to utilize the two-dimensional target detection method to the three-dimensional point cloud target detection, and the improvement of the network in the two-dimensional method will also improve the accuracy of the three-dimensional method.



### 3. Performance of our method 
![捕获5](https://user-images.githubusercontent.com/59796732/133003066-cc425a58-bf07-474e-a295-adb15eb2a1d0.PNG)
We found that in 3D point cloud object detection, with the training time increaseding, Bonet and add-Bonet are more effective than Panet and other feature pyramid methods. Therefore, we believe that our approach has increased the accuracy of Complex Yolo v4 in Kitti dataset. From this results, we learn from that we can use an 2D approach to 3D point clouds and we can try to add residual connection mechanisms to the FPN and improve the accuracy of the model by changing the way that features are fused.






