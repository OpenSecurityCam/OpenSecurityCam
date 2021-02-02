gst-launch-1.0 v4l2src device="/dev/video0" ! videoconvert ! clockoverlay ! x264enc tune=zerolatency ! mpegtsmux ! hlssink target-duration=1 max-files=5
