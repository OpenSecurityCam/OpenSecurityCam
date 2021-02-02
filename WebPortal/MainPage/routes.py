from WebPortal import SocketIOClient
from flask import Blueprint, redirect, url_for, render_template, flash, send_from_directory
from flask_login import current_user
from werkzeug.wrappers import Response

from WebPortal import SocketIOClient
from WebPortal.stateclass import state
from WebPortal.MainPage.Entities.Trigger_Armed_Unarmed.Trigger_Armed_Unarmed import ArmTriggerClass

MainPage = Blueprint('MainPage', __name__)

trigger = ArmTriggerClass(state)

@SocketIOClient.on('Toggle_Arm')
def HandleTrigger():
    trigger.HandleSystemArm()

@MainPage.route('/OneSignalSDKUpdaterWorker.js')
def OneSignalSDKUpdateWorker():
    return MainPage.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKUpdaterWorker.js')

@MainPage.route('/OneSignalSDKWorker.js')
def OneSignalSDKWorker():
    return MainPage.send_static_file('js/OneSignal_Service_Worker/OneSignalSDKWorker.js')

@MainPage.route('/')
def Home():
    if current_user.is_authenticated:
        return render_template('index.html', SystemState = state.SystemState)
    else:
        return redirect(url_for('Authentication.Login'))  

@MainPage.route('/<string:file_name>')
def Stream(file_name):
    video_dir = './videofeed/video'
    return send_from_directory(directory=video_dir, filename=file_name)