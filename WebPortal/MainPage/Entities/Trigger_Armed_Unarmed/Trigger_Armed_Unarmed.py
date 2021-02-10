from flask_socketio import emit

from WebPortal import OneSignalClient
from WebPortal.stateclass import state
from WebPortal.MainPage.Entities.Notifications.Notifications import Notifications
class ArmTriggerClass:
    def HandleSystemArm():
        if state.SystemState:
            self.StateChanger(self, False, Notifications.System_Unarmed_Notification, "UnarmSystem")
        else:
            self.StateChanger(self, True, Notifications.System_Armed_Notification, "ArmSystem")
    
    def StateChanger(self, StateToChange, NotificationType, SocketTrigger):
        state.SystemState = StateToChange
        OneSignalClient.send_notification(NotificationType)
        emit(SocketTrigger, broadcast=True)