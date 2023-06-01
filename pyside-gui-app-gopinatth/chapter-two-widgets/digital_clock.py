# Imports.
import sys
from PySide6.QtCore import QTimer, QDateTime, SIGNAL
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLCDNumber
from PySide6.QtGui import QScreen

class DigitalClock(QWidget):
    """
    Our main window class for Digital clock app.
    """
    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Digital Clock")

        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.updateTime)

        self.timeDisplay = QLCDNumber(self)
        self.timeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.timeDisplay.setDigitCount(12)
        
        self.timeDisplay.resize(500,150)

        self.updateTime()
        self.center()
        timer.start(1000)
        
    
    def center(self) -> None:
        """
        Method to center the application on the screen.
        """
        # Get the screen geometry
        screen_geometry = QScreen.availableGeometry(QApplication.primaryScreen())

        # Calculate the center point
        center_point = screen_geometry.center()

        # Move the window to the center point
        self.move(center_point - self.rect().center())
    
    def updateTime(self)-> None:
        """
        Updates the current time in the LCD display.
        """
        currentTime = QDateTime.currentDateTime().toString("MM/dd/yyyy hh:mm:ss AP")
        # print(f" Current Time : {QDateTime.currentDateTime().toString()}")
        self.timeDisplay.display(currentTime)


def main():
    try:
        app = QApplication()

        digital_clock = DigitalClock()
        digital_clock.show()

        sys.exit(app.exec())
    except NameError as name_error:
        print(f"Name Error : {name_error}")
    except KeyError as key_error:
       print(key_error)
    except Exception as error:
        print(error)
    except SystemExit:
        print("Closing Window ...")
    

if __name__ == "__main__":
    main()