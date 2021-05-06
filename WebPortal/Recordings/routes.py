from flask import Blueprint, redirect, url_for, render_template, flash, send_from_directory
import sys
import os
import datetime
from pathlib import Path

sys.path.append('..')

Recordings = Blueprint('Recordings', __name__)

@Recordings.route('/recordings')
def GetRecordingsList():
    files_in_basepath = list(Path('videos').iterdir())
    files_in_basepath.sort(reverse=True)
    return render_template('recordings.html', recordings_list = files_in_basepath, datetime = datetime)

@Recordings.route('/download/<recording>')
def DownloadRecording(recording):
    path = f"videos/{ recording }"
    return send_from_directory(f"../videos/", recording, as_attachment=True)

@Recordings.route('/delete/<recording>')
def DeleteRecording(recording):
    os.remove(f"videos/{ recording }")
    return redirect(url_for("Recordings.GetRecordingsList"))

@Recordings.route('/watch/<recording>')
def WatchRecording(recording):
    path = f"videos/{ recording }"
    return render_template('watch.html', recording = path)