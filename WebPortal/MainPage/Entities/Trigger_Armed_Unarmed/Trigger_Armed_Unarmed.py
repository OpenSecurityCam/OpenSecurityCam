from flask_socketio import emit

from WebPortal import OneSignalClient
from WebPortal.MainPage.Entities.Notifications.Notifications import Notifications
class ArmTriggerClass:
    def __init__(self, state):
        self.state = state

    def HandleSystemArm(self):
        if self.state.SystemState:
            self.__StateChanger(False, Notifications.System_Unarmed_Notification, "UnarmSystem")
        else:
            self.__StateChanger(True, Notifications.System_Armed_Notification, "ArmSystem")
    
    def __StateChanger(self, StateToChange, NotificationType, SocketTrigger):
        self.state.SystemState = StateToChange
        OneSignalClient.send_notification(NotificationType)
        emit(SocketTrigger, broadcast=True)