import cv2
import random
import numpy as np
import matplotlib.pyplot as plt


def addSpNoise(img_3,sigma):
    rw= img_3.shape[0]
    cl = img_3.shape[1]
    for i in range(0, int((rw * cl) * sigma)):
        num_r = random.randint(0, rw-1)
        num_c = random.randint(0 ,cl-1)
        img_3[num_r][num_c] = [255, 255, 255]
    for i in range(0, int((rw * cl) * sigma)):
        num_r = random.randint(0, rw-1)
        num_c = random.randint(0, cl-1)
        img_3[num_r][num_c] = [0, 0, 0]
    cv2.imwrite("C:\\Users\\tejas\\Desktop\\img\\s&p"+"_"+str(sigma)+".jpg",img_3)


def addGaussNoise(img_1,sigma):
    gauss = np.random.normal(0,sigma,(img_1.shape[0],img_1.shape[1],img_1.shape[2]))
    gauss = gauss.reshape(img_1.shape[0],img_1.shape[1],img_1.shape[2])
    img_1 = img_1 + gauss
    cv2.imwrite("C:\\Users\\tejas\\Desktop\\img\\gauss"+"_"+str(sigma)+".jpg",img_1)

def addSpackleNoise(img_2,sigma):
    spackle=np.random.randn(img_2.shape[0],img_2.shape[1],3)
    spackle=spackle.reshape(img_2.shape[0],img_2.shape[1],3)
    img_2 = img_2 + (img_2*spackle*sigma)
    cv2.imwrite("C:\\Users\\tejas\\Desktop\\img\\spackle"+"_"+str(sigma)+".jpg",img_2)


def convJpeg(img_4,sigma):
    cv2.imwrite("C:\\Users\\tejas\\Desktop\\img\\jpeg"+"_"+str(sigma)+".jpeg",img_4,[cv2.IMWRITE_JPEG_QUALITY,sigma])


img_0 = cv2.imread("C:\\Users\\tejas\\Desktop\\img\\t.jpg")
addSpNoise(img_0,0.001)
addSpNoise(img_0,0.005)
img_0 = cv2.imread("C:\\Users\\tejas\\Desktop\\img\\t.jpg")
addGaussNoise(img_0,0.001)
addGaussNoise(img_0,0.005)
addSpackleNoise(img_0,0.01)
addSpackleNoise(img_0,0.05)
convJpeg(img_0,70)
convJpeg(img_0,90)
