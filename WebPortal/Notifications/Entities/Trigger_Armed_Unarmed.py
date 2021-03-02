from flask_socketio import emit

from WebPortal import OneSignalClient
from WebPortal.stateclass import state
from WebPortal.Notifications.Entities.Notifications import Notifications

class ArmTriggerClass:

    def HandleSystemArm():
        if state.SystemState:
            state.SystemState = False
            OneSignalClient.send_notification(Notifications.System_Unarmed_Notification)
            emit("UnarmSystem", broadcast=True)
        else:
            state.SystemState = True
            OneSignalClient.send_notification(Notifications.System_Armed_Notification)
            emit("ArmSystem", broadcast=True)