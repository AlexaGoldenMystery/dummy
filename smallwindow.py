import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)         #new application is created

    w = QWidget()                       #new window is created
    w.resize(250, 150)                  #300px
    w.setWindowTitle('Simple')          # window title
    w.show()                            #window is going to show

    sys.exit(app.exec_())               #pythonprogramm stops when the appclication (window) stops


if __name__ == '__main__':
    main()