import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore  import Qt


def main ():
    # create the main app instance
    app = QApplication(sys.argv)

    try :
        # create a label and set properties on it
        label = QLabel ()
        label.setText("Hello my first practical/functional approach")
        label.setAlignment(Qt.AlignCenter)
        label.setWindowTitle("First PySide6 app")
        label.setGeometry(100,200,500,300)

        # show app level widget
        label.show()

        # Exit the application
        app.exec()
        sys.exit()
    except NameError:
        print("Name Error :", sys.exc_info()[1])
        ...


if __name__ == "__main__":
    main()
