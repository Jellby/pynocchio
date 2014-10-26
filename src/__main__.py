# -*- coding: UTF-8 -*-

from PySide.QtGui import QApplication
# from PySide.QtCore import QCoreApplication
from main_window import MainWindow


def main():

    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('Pynocchio')
    # QCoreApplication.setApplicationName('Pynocchio')

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
