from PySide6.QtWidgets import QApplication
from dialogs import MainWindow
from auth import Autentificare



if __name__ == "__main__":
    app = QApplication([])

    autentificare = Autentificare()
    main_window = MainWindow()
    main_window.show()
    app.exec()
