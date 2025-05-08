import sys
from frontend.ui import TextFormatter
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextFormatter()
    window.show()
    sys.exit(app.exec_())