import sys, time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(300,250,400,300)


def main():
    try:
        app = QApplication()

        main_window = MainWindow()
        main_window.show()

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