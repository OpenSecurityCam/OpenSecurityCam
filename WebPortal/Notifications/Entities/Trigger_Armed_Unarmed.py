from flask_socketio import emit
import cv2

from WebPortal import OneSignalClient
import sys
import os
import time
sys.path.append('..')
from WebPortal.Notifications.Entities.Notifications import Notifications
from pathlib import Path

class ArmTriggerClass:

    state = False

    def HandleSystemArm(self):
        if self.state:
            self.state = False
            OneSignalClient.send_notification(Notifications.System_Unarmed_Notification)
            emit("UnarmSystem", broadcast=True)
        else:
            self.state = True
            emit("ArmSystem", broadcast=True) 
            for x in range(6):
                files_in_basepath = list(Path('videos/').iterdir())
                files_in_basepath.sort()
                filenum = 0
                if files_in_basepath :
                    filenum = int(files_in_basepath[-1].name.split('.')[0][6:]) + 1
                    print(files_in_basepath[-1].name)
                cap = cv2.VideoCapture(3)
                fourcc = cv2.VideoWriter_fourcc(*'MPEG')
                out = cv2.VideoWriter(f"videos/output{filenum}.mp4",fourcc, 20.0, (640,480))
                OneSignalClient.send_notification(Notifications.System_Armed_Notification)
                time.sleep(5)
                if self.state == False:
                    break
                else:
                    OneSignalClient.send_notification(Notifications.System_Intruder_Notification)
                    
                    while(cap.isOpened()):
                        ret, frame = cap.read()
                        if ret==True:
                            frame = cv2.flip(frame,0)

                            # write the flipped frame
                            out.write(frame)
                            if self.state == False or x == 4:
                                break
                        else:
                            break
                    cap.release()
                    out.release()