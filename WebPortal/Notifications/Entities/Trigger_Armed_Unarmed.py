from flask_socketio import emit

from WebPortal import OneSignalClient
import sys
import time
sys.path.append('..')
from WebPortal.Notifications.Entities.Notifications import Notifications

class ArmTriggerClass:

    state = False

    def HandleSystemArm(self):
        if self.state:
            self.state = False
            OneSignalClient.send_notification(Notifications.System_Unarmed_Notification)
            emit("UnarmSystem", broadcast=True)
        else:
            self.state = True
            OneSignalClient.send_notification(Notifications.System_Armed_Notification)
            emit("ArmSystem", broadcast=True)
            for x in range(6):
                time.sleep(5)
                if self.state == False:
                    break
                else:
                    print(x)
                    OneSignalClient.send_notification(Notifications.System_Intruder_Notification)