import sys
from typing import Optional
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox


class ButtonExample(QWidget):
    def __init__(self, app) -> None:
        super().__init__()

        self.app = app

        self.initGUI()
        self.setButton()

    def initGUI(self):
        self.setWindowTitle("Button Example")
        self.resize(400, 325)

    def quitConfirmation(self, title, message):
        userInfo = QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return True
        if userInfo == QMessageBox.No:
            return False

    def quitApp(self):
        response = self.quitConfirmation("Confirmation","This will quit the application. Do you want to continue?")

        if response == True:
            self.app.quit()
        else: pass


    def setButton(self):
        """
        A function to add a quit button.
        """
        quit_button = QPushButton("Quit",self)
        quit_button.move(50,100)
        quit_button.clicked.connect(self.quitApp)


def main():
    try:
        app = QApplication()

        button_eg = ButtonExample(app)
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