import sys
from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtWidgets import QApplication,QWidget,QPushButton


class DigitalClock(QWidget):
    """
    Digital clock class.
    """
    def __init__(self) -> None:
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Digital Clock")
        self.resize(400, 325)


def main():
    try:
        app = QApplication()

        button_eg = DigitalClock()
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