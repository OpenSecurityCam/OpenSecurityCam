from flask_socketio import emit

from WebPortal import OneSignalClient
import sys
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