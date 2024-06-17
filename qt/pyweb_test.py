import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, url, x, y, width, height, title):
        super().__init__()
        self.browser = QWebEngineView()  # 创建一个 QWebEngineView 对象
        self.browser.setUrl(QUrl(url))  # 设置要加载的网页 URL
        self.setCentralWidget(self.browser)
        self.setGeometry(x, y, width, height)  # 设置窗口位置和大小
        self.setWindowTitle(title)  # 设置窗口标题

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建第一个窗口，放在第一个屏幕上
    window1 = MainWindow("http://localhost:8080/index.html", 0, 0, 1280, 720, 'PyQt5 WebView - Screen 1')
    window1.show()
    
    # 创建第二个窗口，放在第二个屏幕上
    window2 = MainWindow("http://localhost:8080/index4.html", 1280, 0, 1600, 900, 'PyQt5 WebView - Screen 2')
    window2.show()
    
    sys.exit(app.exec_())
