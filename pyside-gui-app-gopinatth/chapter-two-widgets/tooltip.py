import sys
from typing import Optional
from PySide6.QtWidgets import QApplication,QWidget,QLabel
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

        self.set_icon_modes()

    def set_icon_modes (self):
        active_on_icon = QIcon("pyside_logo.png")
        active_on_icon_label = QLabel("Active and On",self)
        active_on_icon_pixamp = active_on_icon.pixmap(50, 50, QIcon.Active, QIcon.On)
        active_on_icon_label.setPixmap(active_on_icon_pixamp )
        active_on_icon_label.show()

        disabled_off_icon = QIcon("pyside_logo.png")
        disabled_off_icon_label = QLabel("Disables and Off",self)
        disabled_off_icon_pixamp = disabled_off_icon.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        disabled_off_icon_label.setPixmap(disabled_off_icon_pixamp )
        disabled_off_icon_label.move(60, 0)
        disabled_off_icon_label.show()

        selected_on_icon = QIcon("pyside_logo.png")
        selected_on_icon_label = QLabel("sample",self)
        selected_on_icon_pixamp = selected_on_icon.pixmap(50, 50, QIcon.Selected, QIcon.On)
        selected_on_icon_label.setPixmap(selected_on_icon_pixamp )
        selected_on_icon_label.move(120, 0)
        selected_on_icon_label.show()

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