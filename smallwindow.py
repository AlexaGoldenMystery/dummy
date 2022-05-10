import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)         #new application is created

    w = QWidget()                       #new window is created
    w.resize(250, 150)                  # size of the window
    w.move(300, 300)                    # window starts at 300, 300px
    w.setWindowTitle('Simple')          # window title
    w.show()                            #window is going to show

    sys.exit(app.exec_())               #pythonprogramm stops when the appclication (window) stops


if __name__ == '__main__':
    main()