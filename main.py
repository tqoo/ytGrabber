from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QGridLayout, QLineEdit, QComboBox, QPushButton, QCheckBox

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

        grabButton = QPushButton("Grab!")
        layout.addWidget(grabButton, 1,0)

        metadataToggle = QCheckBox("Include metadata")
        layout.addWidget(metadataToggle, 1,1)


        self.setFocus()
        self.resize(485,100)
        self.show()
# start the event loop

window = VideoWindow()
app.exec()