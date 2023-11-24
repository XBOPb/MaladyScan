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
        self.ui.scan_url_button.clicked.connect(self.start_url_scan)

    def read_api_key(self):
        self.api_key = self.ui.api_key_field.toPlainText()
        if not self.api_key:
            self.ui.scan_result_area.setText('Please provide your API key first!')

    def scan_result_output(self, scan_result):
        #TODO format json output
        self.ui.scan_result_area.clear()
        self.ui.scan_result_area.setText(scan_result)
    
    def start_file_scan(self):
        self.read_api_key()
        self.file_path = self.ui.file_path_field.toPlainText()
        if not self.file_path:
            file_dialog = QFileDialog()
            self.file_path = QFileDialog.getOpenFileName(file_dialog)[0]
            if not self.file_path:
                return
            self.ui.file_path_field.setText(self.file_path)
        response = v2_api.check_file(self.api_key, self.file_path)
        if response == 403:
            scan_result = 'Unable to authorize scan. Please check if your API key is correct.'
        else:
            scan_result = v2_api.file_check_result(self.api_key, response)
        self.scan_result_output(scan_result)

    def start_url_scan(self):
        self.read_api_key()
        self.url = self.ui.url_address_field.toPlainText()
        if not self.url:
            self.ui.scan_result_area.setText('URL field is empty! Provide a URL to check.')
            return
        response = v2_api.check_link(self.api_key, self.url)
        if not response:
            self.ui.scan_result_area.setText('Please check if your URL is valid.')
        scan_result = v2_api.link_check_result(self.api_key, response)
        self.scan_result_output(scan_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Scanner()
    ui.show()
    app.exec()