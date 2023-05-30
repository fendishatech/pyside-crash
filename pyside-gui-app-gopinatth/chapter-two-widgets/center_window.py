import sys
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QScreen

class CenterWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initGUI()
        self.centerWithQScreen()

    def initGUI(self):
        self.setWindowTitle("Centered Window")
        self.resize(400, 325)

    def centerWithQScreen(self):
        """
        Centers the window using the QDesktop widget.
        """
        # Get the screen geometry
        screen_geometry = QScreen.availableGeometry(QApplication.primaryScreen())

        # Calculate the center point
        center_point = screen_geometry.center()

        print(f"Screen Geometry : {screen_geometry}")
        print(f"Center Point : {center_point}")

        # Move the window to the center point
        self.move(center_point - self.rect().center())

   
def main():
    try:
        app = QApplication()

        button_eg = CenterWindow()
        button_eg.show()

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