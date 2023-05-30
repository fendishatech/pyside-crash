import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication,QWidget,QPushButton


class ButtonExample(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Button Example")
        self.resize(400, 325)


def main():
    try:
        app = QApplication()

        button_eg = ButtonExample()
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