import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import pyqtSlot

class ClickableLabel(QLabel):
    def __init__(self, message, parent=None):
        super(ClickableLabel, self).__init__(message, parent)
        self.count = 0

    def mousePressEvent(self, event):
        self.count += 1
        self.setText("Click count: {0}".format(self.count))  # 修改这里使用str.format()

def create_window(x, y, width, height, message):
    window = QWidget()
    window.setWindowTitle("PyQt Window")
    window.setGeometry(x, y, width, height)
    label = ClickableLabel(message, window)
    label.move(50, 50)
    window.show()
    return window

app = QApplication(sys.argv)

# Set the position and size of the windows according to the displays
window1 = create_window(0, 0, 1280, 720, "Content on internal display (eDP-1)")
window2 = create_window(1280, 0, 1600, 900, "Content on HDMI monitor (HDMI-1)")

sys.exit(app.exec_())

