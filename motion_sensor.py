from gpiozero import LED
from gpiozero import MotionSensor
import time
import keyboard
import cv2

warningLED = LED(17)
sensor = MotionSensor(4)

TimesFlashingSet = input("Enter how many times the led has to flash: ")
FlashingDelay = input("Enter the delay between flashes: ")

def LEDFlashing():

	warningLED.on()
	time.sleep(5)
	warningLED.off()

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        cv2.imshow('maina', img)
        if cv2.waitKey(1) & keyboard.is_pressed('q'): 
            break

    cv2.destroyAllWindows()
    

def MotionDetection():
	while True:
		sensor.wait_for_motion()
		print("Detected")
		LEDFlashing()
		show_webcam(True)
		if keyboard.is_pressed('q'):
			break

MotionDetection()
