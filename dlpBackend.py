from yt_dlp import YoutubeDL
from pprint import pprint
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal
class Grabber(QObject):
    progressSig = pyqtSignal(int)
    finished = pyqtSignal()
    def __init__(self, URL):
        super().__init__()
        self.url = URL
        self.progress = 0
        self.thumbnail = ""
    def download(self):
        ydl_opts = {
            'progress_hooks': [self.progress_hook],
            "keep": False
        }

        with YoutubeDL(ydl_opts) as ydl:
            self.metadata = ydl.extract_info(self.url, download=True)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if "total_bytes" in d:
                self.progress = d["downloaded_bytes"]/d["total_bytes"]
            else:
                self.progress = d["downloaded_bytes"]/d["total_bytes_estimate"]
                if self.progress != 1.0:
                    self.progressSig.emit(int(self.progress*100))
                
        elif d["status"] == "finished":
            print("Done!")

