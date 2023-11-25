# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color:  qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #999, stop: 1 #111\n"
"        );")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.general_lay = QtWidgets.QVBoxLayout()
        self.general_lay.setObjectName("general_lay")
        self.title_api_lay = QtWidgets.QHBoxLayout()
        self.title_api_lay.setObjectName("title_api_lay")
        self.api_key_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.api_key_label.setFont(font)
        self.api_key_label.setStyleSheet("background: transparent; color: rgb(255, 255, 255);")
        self.api_key_label.setObjectName("api_key_label")
        self.title_api_lay.addWidget(self.api_key_label)
        self.api_key_field = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.api_key_field.setMaximumSize(QtCore.QSize(16777215, 30))
        self.api_key_field.setStyleSheet("QTextEdit {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"\n"
"    }\n"
"\n"
"QTextEdit:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QTextEdit:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.api_key_field.setObjectName("api_key_field")
        self.title_api_lay.addWidget(self.api_key_field)
        self.general_lay.addLayout(self.title_api_lay)
        self.main_lay = QtWidgets.QHBoxLayout()
        self.main_lay.setObjectName("main_lay")
        self.file_lay = QtWidgets.QVBoxLayout()
        self.file_lay.setObjectName("file_lay")
        self.file_path_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.file_path_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.file_path_label.setFont(font)
        self.file_path_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.file_path_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.file_path_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.file_path_label.setObjectName("file_path_label")
        self.file_lay.addWidget(self.file_path_label)
        self.file_path_field = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.file_path_field.setMaximumSize(QtCore.QSize(16777215, 30))
        self.file_path_field.setStyleSheet("QTextEdit {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"\n"
"    }\n"
"\n"
"QTextEdit:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QTextEdit:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.file_path_field.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.file_path_field.setObjectName("file_path_field")
        self.file_lay.addWidget(self.file_path_field)
        self.scan_file_button = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.scan_file_button.setFont(font)
        self.scan_file_button.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.scan_file_button.setObjectName("scan_file_button")
        self.file_lay.addWidget(self.scan_file_button)
        self.main_lay.addLayout(self.file_lay)
        self.url_lay = QtWidgets.QVBoxLayout()
        self.url_lay.setObjectName("url_lay")
        self.url_address_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.url_address_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.url_address_label.setFont(font)
        self.url_address_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.url_address_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.url_address_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.url_address_label.setObjectName("url_address_label")
        self.url_lay.addWidget(self.url_address_label)
        self.url_address_field = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.url_address_field.setMaximumSize(QtCore.QSize(16777215, 30))
        self.url_address_field.setStyleSheet("QTextEdit {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"\n"
"    }\n"
"\n"
"QTextEdit:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QTextEdit:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.url_address_field.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.url_address_field.setObjectName("url_address_field")
        self.url_lay.addWidget(self.url_address_field)
        self.scan_url_button = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.scan_url_button.setFont(font)
        self.scan_url_button.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.scan_url_button.setObjectName("scan_url_button")
        self.url_lay.addWidget(self.scan_url_button)
        self.main_lay.addLayout(self.url_lay)
        self.ip_lay = QtWidgets.QVBoxLayout()
        self.ip_lay.setObjectName("ip_lay")
        self.ip_address_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ip_address_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.ip_address_label.setFont(font)
        self.ip_address_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.ip_address_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.ip_address_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ip_address_label.setObjectName("ip_address_label")
        self.ip_lay.addWidget(self.ip_address_label)
        self.ip_address_field = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ip_address_field.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ip_address_field.setStyleSheet("QTextEdit {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"\n"
"    }\n"
"\n"
"QTextEdit:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QTextEdit:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.ip_address_field.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.ip_address_field.setObjectName("ip_address_field")
        self.ip_lay.addWidget(self.ip_address_field)
        self.scan_ip_button = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.scan_ip_button.setFont(font)
        self.scan_ip_button.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.scan_ip_button.setObjectName("scan_ip_button")
        self.ip_lay.addWidget(self.scan_ip_button)
        self.main_lay.addLayout(self.ip_lay)
        self.general_lay.addLayout(self.main_lay)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 774, 369))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scan_result_area = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.scan_result_area.setStyleSheet("color: rgb(200, 200, 200);")
        self.scan_result_area.setText("")
        self.scan_result_area.setObjectName("scan_result_area")
        self.gridLayout_2.addWidget(self.scan_result_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.general_lay.addWidget(self.scrollArea)
        self.general_lay.setStretch(1, 3)
        self.general_lay.setStretch(2, 7)
        self.gridLayout.addLayout(self.general_lay, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MaladyScan"))
        self.api_key_label.setText(_translate("MainWindow", "API Key:"))
        self.file_path_label.setText(_translate("MainWindow", "File path:"))
        self.scan_file_button.setText(_translate("MainWindow", "Scan File"))
        self.url_address_label.setText(_translate("MainWindow", "URL address:"))
        self.scan_url_button.setText(_translate("MainWindow", "Scan URL"))
        self.ip_address_label.setText(_translate("MainWindow", "IP address:"))
        self.scan_ip_button.setText(_translate("MainWindow", "Scan IP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
