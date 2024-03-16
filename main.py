from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QThread
import dlpBackend, threading
app = QApplication([])

class VideoWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyGrabber')
        layout = QGridLayout()
        self.setLayout(layout)

        videoURLbox = QLineEdit()
        videoURLbox.setPlaceholderText("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        layout.addWidget(videoURLbox, 0,0)

        videoFormatDropdown = QComboBox()
        videoFormatDropdown.addItems(["mp4","mov","avi","webm"])
        layout.addWidget(videoFormatDropdown, 0,1)

        self.grabButton = QPushButton("Grab!")
        self.grabButton.clicked.connect(self.grab_video)
        layout.addWidget(self.grabButton, 1,0)

        metadataToggle = QCheckBox("Include metadata")
        layout.addWidget(metadataToggle, 1,1)

        self.statusScrollBox = QScrollArea()
        self.scrollContainerWidget = QWidget()
        self.scrollBoxLayout = QVBoxLayout()
        self.scrollContainerWidget.setLayout(self.scrollBoxLayout)
        self.statusScrollBox.setWidget(self.scrollContainerWidget)
        self.statusScrollBox.setWidgetResizable(True)

        layout.addWidget(self.statusScrollBox, 2, 0, 2, 0)
        self.setFocus()
        self.resize(485,100)
        self.show()

    def grab_video(self):
        videoStatusWidget = VideoDownloaderStatus("a","https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.scrollBoxLayout.addWidget(videoStatusWidget)
        videoStatusWidget.grab_video()


class VideoDownloaderStatus(QWidget):
    def __init__(self, img, title):
        super().__init__()
        self.videoTitle = title
        self.videoThumb = img
        mainLayout = QHBoxLayout()
        infoLayout = QGridLayout()

        videoThumbLabel = QLabel()
        #videoThumbLabel.setPixmap(self.videoThumb)
        mainLayout.addWidget(videoThumbLabel)
        mainLayout.addLayout(infoLayout)
        
        videoName = QLabel(self.videoTitle)
        videoNameFont = QFont()
        videoNameFont.setBold(True)
        videoNameFont.setPixelSize(10)
        videoName.setFont(videoNameFont)
        infoLayout.addWidget(videoName,0,0)

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0,100)
        self.progressBar.setValue(0)
        #self.progressBar.valueChanged.connect(lambda: app.processEvents() )
        infoLayout.addWidget(self.progressBar,1,0)
        
        self.setLayout(mainLayout)
        self.show()

    def grab_video(self):
        # pass on to "backend"
        self.thread = QThread()
        self.grabber = dlpBackend.Grabber("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        self.grabber.moveToThread(self.thread)

        self.thread.started.connect(self.grabber.download)
        self.grabber.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.grabber.progressSig.connect(self.setProgress)

        self.progressBar.setValue(0)
        self.thread.start()

    def setProgress(self, value):
        if value > self.progressBar.value():
            self.progressBar.setValue(value)
        app.processEvents()

# start the  loop

window = VideoWindow()
app.exec()