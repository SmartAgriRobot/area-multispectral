import cv2
import threading
import numpy as np
from aspectral_lib import *
from time import sleep
from gpiozero import LED

def process_image(im):
	global fShow, fExit
	if fShow == False:
		contrasted = contrast_stretch(im)
		ndvi = calc_ndvi(contrasted)
		ndvi_contrasted = contrast_stretch(ndvi)
		color_mapped_prep = ndvi_contrasted.astype(np.uint8)
		color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
		crop_imgage = color_mapped_image[48:432, 0:640]
		crop_imgage = cv2.flip(crop_imgage, 1)
		image_resized = image_resize(crop_imgage, width = 800)
		cv2.putText(image_resized, 'NDVI Image', (350, 20), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
		cv2.imshow('NDVI Sensor', image_resized)
		k = cv2.waitKey(1)
		if k==27:
			fExit = True
			return	
		fShow = True

ir_led = LED(17)
ir_led.off()
sleep(0.5)

fShow = True
fExit = False

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture('libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! videoscale ! appsink max-buffers=1 drop=true', cv2.CAP_GSTREAMER)

if not cap.isOpened():
	print('VideoCapture not opened')
	exit(0)

while True:
	if fShow:
		fShow = False
		ret,frame = cap.read()

		if not ret:
			print('empty frame')
			break
		
		thread = threading.Thread(target=process_image, args=(frame,))
		thread.start()

	if fExit:
		break

cv2.destroyAllWindows()