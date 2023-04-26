import sys
from PySide6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    
    def __init__ (self)->None:
        super().__init__()
        self.setWindowTitle("My First PySide App")

        # set size
        self.resize(200,150)


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # Exit the app
    sys.exit(app.exec())

if __name__ == "__main__":
    main()