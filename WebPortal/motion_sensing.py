import sys
sys.path.append('..')
from gpiozero import MotionSensor
import time
import keyboard
from WebPortal import OneSignalClient
from WebPortal.Notifications.Entities.Notifications import Notifications
sensor = MotionSensor(4)



while True:
	sensor.wait_for_motion()
	OneSignalClient.send_notification(Notifications.System_Intruder_Notification)
	print("Detected")
	if keyboard.is_pressed('q'):
		break