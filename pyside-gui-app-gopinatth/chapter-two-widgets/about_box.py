import sys
from typing import Optional
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox


class ButtonExample(QWidget):
    def __init__(self, app) -> None:
        super().__init__()

        self.app = app

        self.initGUI()
        self.aboutButton()

    def initGUI(self):
        self.setWindowTitle("Button Example")
        self.resize(400, 325)

    def showAboutWindow(self):
        """
        Function to show about window.
        """
        QMessageBox.about(self.about_button, "About", "We are dedicated developers.")
        
    def aboutButton(self):
        """
        A function to add a about button.
        """
        self.about_button = QPushButton("About",self)
        self.about_button.move(50,100)
        self.about_button.clicked.connect(self.showAboutWindow)


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