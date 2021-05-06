import keyboard
import sys 
sys.path.append('../../..')
from WebPortal.Notifications.Entities.Notifications import Notifications
from WebPortal.Notifications.routes import armTriggerClass

print(armTriggerClass.state)
while armTriggerClass.state:
    print(armTriggerClass.state)
    delay(50)
    if armTriggerClass.state == False:
        break