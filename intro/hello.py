import sys
from PySide2.QtWidgets import QApplication, QLabel, QWidget


class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Hello World!", self)
        self.label.setGeometry(50, 50, 200, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    hello = HelloWorld()
    hello.show()

    sys.exit(app.exec_())