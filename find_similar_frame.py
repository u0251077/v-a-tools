from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import  array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from sklearn.metrics.pairwise import cosine_similarity
from skimage import data
from skimage import img_as_float
from skimage import measure
import numpy as np
import argparse
import cv2

def PSNR2(y_true, y_pred):
    assert y_true.shape == y_pred.shape, "Cannot calculate PSNR. Input shapes not same." \
                                             " y_true shape = %s, y_pred shape = %s" % (str(y_true.shape),
                                                                                   str(y_pred.shape))
    return -10. * np.log10(np.mean(np.square(y_pred - y_true)))

def img2np(filename):
	img = load_img(filename)# this is a PIL image
	x = img_to_array(img) # this is a Numpy array with shape (3, ?, ?)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, ?, ?)
	x = x.astype('float32') / 255.

	return x

def imgresize2np(filename):
	img = load_img(filename,target_size=(args.predict_h, args.predict_w))# this is a PIL image
	img.save("../image/resizenir.png")
	x = img_to_array(img) # this is a Numpy array with shape (3, ?, ?)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, ?, ?)
	x = x.astype('float32') / 255.

	return x


class Metric ():
	def calculatePSNR(self, gt, predict):
		"""Calculate PSNR function between two images.

		Args:
			gt: ground truth image path.
			predict: predict(being compared) image path.

		Returns:
			The return float value [0,Positive infinite]. This value represents how many dB of PSNR.
			This more large the value is , the better.

		"""
		img1 = img2np(gt)
		img2 = img2np(predict)
		return PSNR2(img1,img2)

	def calculateSSIM(self, gt, predict):
		"""Calculate SSIM function between two images.

		Args:
			gt: ground truth image path.
			predict: predict(being compared) image path.

		Returns:
			The return float value [0,1]. This value represents how many Similarity of luminance, contrast and structure.
			This more closer to 1 the value is, the better.

		"""		
		ssim_img1 = cv2.imread(gt, 1)
		ssim_img2 = cv2.imread(predict, 1)
		return measure.compare_ssim(ssim_img1, ssim_img2, multichannel=True)

	def calculateMSE(self, gt, predict):
		"""Calculate MSE(Mean-Square Error) function between two images.

		Args:
			gt: ground truth image path.
			predict: predict(being compared) image path.

		Returns:
			The return float value [0,Positive  infinite]. This value represents the Mean-Square Error between the two image.
			This more closer to 0 the value is, the better.

		"""			
		img1 = img2np(gt)
		img2 = img2np(predict)
		return np.mean(np.square(img2 - img1))

	def calculateCosSim(self, gt, predict):
		"""Calculate cosine similarity function between two images.

		Args:
			gt: ground truth image path.
			predict: predict(being compared) image path.

		Returns:
			The return float value [0,1]. This value represents the cosine similarity between the two image.
			This more closer to 0 the value is, the better.

		"""			
		img1 = img2np(gt)
		img2 = img2np(predict)
		img1=np.reshape(img1,(1,img1.shape[1]*img1.shape[2]*img1.shape[3]))
		img2=np.reshape(img2,(1,img2.shape[1]*img2.shape[2]*img2.shape[3]))
		cos_sim = cosine_similarity(img1,img2)
		return cos_sim[0][0]
import os
ds=1
gt = "./data/frame"+str(ds)+".png"
for i in range(0,279):
	print("rank :", i+1)
	gt = "./data/frame"+str(ds)+".png"
	ds=ds+4
	M = Metric()
	print("now file is :",gt)
	yourPath = './similar/'
	allFileList = os.listdir(yourPath)
	arraysss={}
	c = 0

	for file in allFileList:
	    c=c+1
	    predict = yourPath+file
	    result = M.calculateMSE(gt,predict)
	    arraysss[predict]= result
	f = 0
	for k, v in sorted(arraysss.items(), key=lambda item: item[1]):
	    print("seem to :",k,v)
	    if f ==1:
	        a = cv2.imread(k,1)
	        na = "./cp2/"+str(i+1)+".jpg"
	        cv2.imwrite(na,a)
	        break
	    f=f+1
