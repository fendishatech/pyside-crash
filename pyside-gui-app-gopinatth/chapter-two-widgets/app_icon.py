import sys
from typing import Optional
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QIcon

class AppIconExample(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initGUI()
    
    def initGUI(self):
        self.setWindowTitle("App Icon Example")
        self.resize(400, 325)

        app_icon = QIcon("pyside_logo.png")
        self.setWindowIcon(app_icon)


def main():
    try:
        app = QApplication(sys.argv)

        main_window = AppIconExample()
        main_window.show()
        
        # Exit the app
        sys.exit(app.exec())

    except NameError as name_error:
       print(name_error)
    except KeyError as key_error:
       print(key_error)
    except Exception as error:
        print(error)
    except SystemExit:
        print("Closing Window ...")

if __name__ == "__main__":
    main()