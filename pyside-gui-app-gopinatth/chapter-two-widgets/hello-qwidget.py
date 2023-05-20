import sys, time
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QCoreApplication
import traceback

class SampleWindow(QWidget):
    
    def __init__ (self)->None:
        super().__init__()
        self.setWindowTitle("My First PySide App")

        self.initGUI

    def initGUI(self):
        self.setWindowTitle("Sample Window")
        self.setGeometry(300,300,200,150)
        self.setMinimumHeight(200)
        self.setMinimumWidth(100)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)
        print("Sample window")
        
def print_error_details(error):
    # I want this to work for 
    # TypeError, ValueError, AttributeError, IndexError, KeyError, SyntaxError, IndentationError, FileNotFoundError
    
    # get the traceback information
    tb = traceback.format_exc()
    # get the line number where the error occurred
    line_number = traceback.extract_tb(error.__traceback__)[-1][1]
    # get the name of the variable that caused the error
    variable_name = error.args[0].split("'")[1]
    # print the error message with relevant information
    print(f"Error: {error.__class__.__name__} \n Description : {variable_name} is not defined \n Line : on line {line_number}")

def main():
    try:
        app = QApplication(sys.argv)

        QCoreApplication.processEvents()
        main_window = SampleWindow()
        main_window.show()
        time.sleep(3)

        main_window.resize(300,300)
        main_window.setWindowTitle("When will i see you again")
        main_window.repaint()
        main_window.show()
        
        # Exit the app
        sys.exit(app.exec())

    except NameError as name_error:
       print_error_details(name_error)
    except KeyError as key_error:
       print_error_details(key_error)
    except Exception as error:
        print(error)
    except SystemExit:
        print("Closing Window ...")


if __name__ == "__main__":
    main()