import sys
import datetime
from pathlib import Path

sys.path.append('..')

files_in_basepath = list(Path('../../../videos').iterdir())
files_in_basepath.sort(reverse=True)
filenum = -1
for file in files_in_basepath:
    if file.is_file():
        print(str(datetime.datetime.fromtimestamp(file.stat().st_mtime))[:19])