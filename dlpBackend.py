from yt_dlp import YoutubeDL
from pprint import pprint

class Grabber():
    def __init__(self, URL, progressBar):
        self.url = URL
        self.progress = 0
        self.thumbnail = ""
        self.progressBar = progressBar
        print(progressBar.__dict__)
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
                self.progressBar.setValue(int(self.progress*100))
                
        elif d["status"] == "finished":
            print("Done!")

