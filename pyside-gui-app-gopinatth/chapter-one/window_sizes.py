import sys
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy


class MainWindow(QWidget):
    # This is the main container window level widget
    def __init__ (self)->None:
        super().__init__()

        # self.setWindowOpacity(0.5) # Sets the window opacity to 50%

        self.setWindowTitle("Ways to size window in PySide")
        # WAYS TO SIZE 
        
        # Using resize
        # self.resize(720,540)

        # Fixed size
        # self.setFixedSize(800, 600)

        # Maximum and Minimum sizes
        # self.setMinimumSize(400, 300)
        # self.setMaximumSize(1200, 900)

        # Using sized policy
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # setting setGeometry(x,y,width,height)
        # x : where the window starts in the x direction of the monitor
        # y : where the window starts in the y direction of the monitor
        # width followed by a height
        self.setGeometry(200,200,800,400)

        # Using StyleSheet or qss
        # self.setObjectName("main-window")
        # self.setStyleSheet("#main-window { width: 300px;height:300px; }")
        # self.setStyleSheet("#main-window { height:300px; min-width: 500px; max-width: 900px;}")

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # Exit the app
    sys.exit(app.exec())

if __name__ == "__main__":
    main()