from gpiozero import LED
from gpiozero import MotionSensor
import time
import keyboard
from WebPortal import OneSignalClient
from WebPortal.MainPage.routes import SystemState
from WebPortal.Notifications.Entities.Notifications import Notifications

warningLED = LED(17)
sensor = MotionSensor(4)

print("Script started")

def LEDFlashing():
	warningLED.on()
	time.sleep(5)
	warningLED.off()


def MotionDetection():
	while True:
		print(SystemState)
		if SystemState:
			sensor.wait_for_motion()
			OneSignalClient.send_notification(Notifications.System_Intruder_Notification)
			print("Detected")
			LEDFlashing()
			if keyboard.is_pressed('q'):
				break

MotionDetection()
