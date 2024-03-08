from yt_dlp import YoutubeDL

class Grabber():
    def __init__(self, URL):
        self.url = URL
        pass
    def download(self):
        #download stuff
        #bind self.progress to a yt_dlp progress_hook
        pass
    def grabMetadata(self):
        #get video/audio metadata and spit out the response
        #then main.py will plonk that data into videoDownloaderStatus
        pass