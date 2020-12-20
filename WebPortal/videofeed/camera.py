import cv2
class Cam:
    def __init__(self, camera_num):
        self.video = cv2.VideoCapture(camera_num)

    def GetAFrame(self):
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tostring()