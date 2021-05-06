from flask import Blueprint

from WebPortal import SocketIOClient
from WebPortal.Notifications.Entities.Trigger_Armed_Unarmed import ArmTriggerClass

Notifications = Blueprint('Notifications', __name__)

armTriggerClass = ArmTriggerClass()

# Handles the ArnSystem button using WebSockets
@SocketIOClient.on('Toggle_Arm')
def HandleTrigger():
    armTriggerClass.HandleSystemArm()

# returns the update worker for the Onesignal notification service
@Notifications.route('/OneSignalSDKUpdaterWorker.js')
def OneSignalSDKUpdateWorker():
    return Notifications.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKUpdaterWorker.js')

# returns the service worker for the Onesignal notification service
@Notifications.route('/OneSignalSDKWorker.js')
def OneSignalSDKWorker():
    return Notifications.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKWorker.js')
