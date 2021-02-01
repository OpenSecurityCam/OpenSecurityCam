from WebPortal import SocketIOClient
from flask import Blueprint, redirect, url_for, render_template, flash, send_from_directory
from flask_socketio import send, emit
from flask_login import current_user
from werkzeug.wrappers import Response
from onesignal_sdk.client import Client

from WebPortal import SocketIOClient

main = Blueprint('main', __name__)

OneSignalClient = Client(app_id="68c16cd3-65dd-4d94-ae7a-550e64acb7e4", rest_api_key="ZDZkZWZjY2QtYTk5Ni00NjBlLWFiYjktZDcxMzRlYTA1NzBk")

class StateClass:
    SystemState = False

state = StateClass()

System_Armed_Notification = {
    'contents': {'en': 'The system is currently ARMED'},
    'included_segments': ['All'],
}

System_Unarmed_Notification = {
    'contents': {'en': 'The system is currently UNARMED'},
    'included_segments': ['All'],
}

@SocketIOClient.on('Toggle_Arm')
def HandleSystemArm():
    if state.SystemState:
        state.SystemState = False
        print(state.SystemState)
        OneSignalClient.send_notification(System_Unarmed_Notification)
        emit("UnarmSystem", "Unarm System", broadcast=True)
    else:
        state.SystemState = True
        OneSignalClient.send_notification(System_Armed_Notification)
        print(state.SystemState)
        emit("ArmSystem", "Arm System", broadcast=True)

@main.route('/OneSignalSDKUpdaterWorker.js')
def OneSignalSDKUpdateWorker():
    return main.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKUpdaterWorker.js')

@main.route('/OneSignalSDKWorker.js')
def OneSignalSDKWorker():
    return main.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKWorker.js')

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html', SystemState = state.SystemState)
    else:
        return redirect(url_for('authentication.login'))  

@main.route('/<string:file_name>')
def stream(file_name):
    video_dir = './videofeed/video'
    return send_from_directory(directory=video_dir, filename=file_name)