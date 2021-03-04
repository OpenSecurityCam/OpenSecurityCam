from flask_socketio import emit

from WebPortal import OneSignalClient
import sys
sys.path.append('..')
from stateClass import State
from WebPortal.Notifications.Entities.Notifications import Notifications

class ArmTriggerClass:

    def HandleSystemArm():
        if State.state:
            State.state = False
            OneSignalClient.send_notification(Notifications.System_Unarmed_Notification)
            emit("UnarmSystem", broadcast=True)
        else:
            State.state = True
            OneSignalClient.send_notification(Notifications.System_Armed_Notification)
            emit("ArmSystem", broadcast=True)