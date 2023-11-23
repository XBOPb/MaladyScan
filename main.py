import sys
import v2_api
from user_interface import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

class Scanner(QMainWindow):
    def __init__(self):
        super(Scanner, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api_key = None

        self.ui.scan_file_button.clicked.connect(self.start_file_scan)

    def read_api_key(self):
        self.api_key = self.ui.api_key_field.toPlainText()

    def start_file_scan(self):
        self.read_api_key()
        self.file_path = self.ui.file_path_field.toPlainText()
        if not self.file_path:
            file_dialog = QFileDialog()
            self.file_path = QFileDialog.getOpenFileName(file_dialog)[0]
            self.ui.file_path_field.setText(self.file_path)
        response = v2_api.check_file(self.file_path)
        if response == 403:
            self.ui.scan_result_Area.setText('Unable to authorize scan. Please check if your API key is correct.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Scanner()
    ui.show()
    app.exec()