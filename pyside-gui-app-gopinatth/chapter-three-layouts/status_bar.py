import sys, time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QProgressBar, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.initGUI()

    def initGUI(self) -> None:
        self.setWindowTitle("Status Bar")
        self.statusLabel = QLabel()
        self.setGeometry(300,250,400,300)
        self.createProgressBar()
        self.createStatusBar()
        for i in range (0, 102, 2):
            self.showProgressBar(i)
            time.sleep(0.1)

    def createStatusBar(self)->None:
        """
        A method to create a a status bar to our main window.
        """
        self.newStatusBar = QStatusBar()
        # self.newStatusBar.showMessage("Ready",2000)
        self.newStatusBar.addWidget(self.statusLabel, 1)
        self.newStatusBar.addWidget(self.newProgressBar, 2)
        self.setStatusBar(self.newStatusBar)

    def createProgressBar(self)->None:
        """
        A method to create a a status bar to our main window.
        """
        self.newProgressBar = QProgressBar()
        self.newProgressBar.setMinimum(0)
        self.newProgressBar.setMaximum(100)

    def showProgressBar(self, progress)-> None :
        """
        Shows the progress bat with a label inside the status bar.
        """
        self.newProgressBar.setValue(progress)
        if progress == 100 :
            self.statusLabel.setText("Ready")
            return
        


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