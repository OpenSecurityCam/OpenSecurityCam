import cv2
class Cam:
    def get_frames():
        video = cv2.VideoCapture(0)

        while True:
            ret, frame = video.read()

            ret, jpeg = cv2.imencode('.jpg', frame)

            frame = jpeg.tostring()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
        del(video)