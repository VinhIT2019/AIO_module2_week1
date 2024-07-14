#Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Lightness:
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('dog.jpeg')
gray_img_01 = (np.max(img,axis = 2)+np.min(img,axis=2))/2
print(gray_img_01[0,0])

#Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Average:
gray_img_02 = np.average(img,axis = 2)
print(gray_img_02[0,0])

#Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Luminosity:
gray_img_03 = 0.21*img[:,:,0]+0.72*img[:,:,1]+0.07*img[:,:,2]
print(gray_img_03[0,0])


