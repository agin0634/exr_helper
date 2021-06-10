# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 580)
        MainWindow.setMinimumSize(QtCore.QSize(780, 580))
        MainWindow.setMaximumSize(QtCore.QSize(780, 580))
        MainWindow.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 701, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 45))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.label_4.setObjectName("label_4")
        self.BuildNumber = QtWidgets.QLabel(self.widget_2)
        self.BuildNumber.setGeometry(QtCore.QRect(190, 20, 47, 16))
        self.BuildNumber.setStyleSheet("color: rgb(92, 92, 92);")
        self.BuildNumber.setObjectName("BuildNumber")
        self.verticalLayout.addWidget(self.widget_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border: 1px solid gray; \n"
"    margin-top:7px;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    subcontrol-origin: margin;\n"
"    color: rgb(255, 255, 255);\n"
"     subcontrol-position: top center; /* position at the top left*/ \n"
"     padding:0 3px;\n"
" } ")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 681, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(71, 16777215))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.InFolderPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.InFolderPath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.InFolderPath.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.InFolderPath.setObjectName("InFolderPath")
        self.horizontalLayout.addWidget(self.InFolderPath)
        self.InFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.InFolderButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.InFolderButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.InFolderButton.setObjectName("InFolderButton")
        self.horizontalLayout.addWidget(self.InFolderButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.checking_R = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checking_R.setMaximumSize(QtCore.QSize(35, 16777215))
        self.checking_R.setStyleSheet("border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.checking_R.setChecked(True)
        self.checking_R.setTristate(False)
        self.checking_R.setObjectName("checking_R")
        self.horizontalLayout_5.addWidget(self.checking_R)
        self.checking_G = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checking_G.setMaximumSize(QtCore.QSize(35, 16777215))
        self.checking_G.setStyleSheet("border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.checking_G.setTristate(False)
        self.checking_G.setObjectName("checking_G")
        self.horizontalLayout_5.addWidget(self.checking_G)
        self.checking_B = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checking_B.setMaximumSize(QtCore.QSize(35, 16777215))
        self.checking_B.setStyleSheet("border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.checking_B.setTristate(False)
        self.checking_B.setObjectName("checking_B")
        self.horizontalLayout_5.addWidget(self.checking_B)
        self.checking_A = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checking_A.setMaximumSize(QtCore.QSize(35, 16777215))
        self.checking_A.setStyleSheet("border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.checking_A.setTristate(False)
        self.checking_A.setObjectName("checking_A")
        self.horizontalLayout_5.addWidget(self.checking_A)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.StartFrame = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.StartFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.StartFrame.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.StartFrame.setMaximum(999999999)
        self.StartFrame.setObjectName("StartFrame")
        self.horizontalLayout_5.addWidget(self.StartFrame)
        self.EndFrame = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.EndFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.EndFrame.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.EndFrame.setMaximum(999999999)
        self.EndFrame.setObjectName("EndFrame")
        self.horizontalLayout_5.addWidget(self.EndFrame)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.CheckButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.CheckButton.setEnabled(True)
        self.CheckButton.setMinimumSize(QtCore.QSize(100, 0))
        self.CheckButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CheckButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.CheckButton.setCheckable(False)
        self.CheckButton.setObjectName("CheckButton")
        self.horizontalLayout_6.addWidget(self.CheckButton)
        self.StopCheckButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.StopCheckButton.setMinimumSize(QtCore.QSize(100, 0))
        self.StopCheckButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.StopCheckButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.StopCheckButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.StopCheckButton.setObjectName("StopCheckButton")
        self.horizontalLayout_6.addWidget(self.StopCheckButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"    border: 1px solid gray; \n"
"    margin-top:7px;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    subcontrol-origin: margin;\n"
"    color: rgb(255, 255, 255);\n"
"     subcontrol-position: top center; /* position at the top left*/ \n"
"     padding:0 3px;\n"
" } ")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 681, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.OutFolderPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.OutFolderPath.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.OutFolderPath.setObjectName("OutFolderPath")
        self.horizontalLayout_2.addWidget(self.OutFolderPath)
        self.OutFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.OutFolderButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.OutFolderButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.OutFolderButton.setObjectName("OutFolderButton")
        self.horizontalLayout_2.addWidget(self.OutFolderButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setMinimumSize(QtCore.QSize(71, 0))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.OutputOption = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.OutputOption.setMinimumSize(QtCore.QSize(150, 0))
        self.OutputOption.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.OutputOption.setObjectName("OutputOption")
        self.horizontalLayout_3.addWidget(self.OutputOption)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.Unchecked = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.Unchecked.setStyleSheet("border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.Unchecked.setObjectName("Unchecked")
        self.horizontalLayout_3.addWidget(self.Unchecked)
        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.StartButton.setMinimumSize(QtCore.QSize(100, 0))
        self.StartButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_3.addWidget(self.StartButton)
        self.StopOutButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.StopOutButton.setMinimumSize(QtCore.QSize(100, 0))
        self.StopOutButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.StopOutButton.setObjectName("StopOutButton")
        self.horizontalLayout_3.addWidget(self.StopOutButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.plain = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plain.setMaximumSize(QtCore.QSize(16777215, 200))
        self.plain.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.plain.setReadOnly(True)
        self.plain.setObjectName("plain")
        self.verticalLayout.addWidget(self.plain)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.OutFolderButton.clicked.connect(MainWindow.eventOutFolderBrowse)
        self.InFolderButton.clicked.connect(MainWindow.eventInFolderBrowse)
        self.CheckButton.clicked.connect(MainWindow.eventFilesCheck)
        self.pushButton_3.clicked.connect(MainWindow.eventClearLog)
        self.StopCheckButton.clicked.connect(MainWindow.eventStopCheck)
        self.StartButton.clicked.connect(MainWindow.eventStartOutput)
        self.StopOutButton.clicked.connect(MainWindow.eventStopOutput)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">EXR</span><span style=\" font-size:26pt;\"> helper</span></p></body></html>"))
        self.BuildNumber.setText(_translate("MainWindow", "v1.0.0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Input File"))
        self.label.setText(_translate("MainWindow", "Input Folder:    "))
        self.InFolderButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Checking Channels:"))
        self.checking_R.setText(_translate("MainWindow", "R"))
        self.checking_G.setText(_translate("MainWindow", "G"))
        self.checking_B.setText(_translate("MainWindow", "B"))
        self.checking_A.setText(_translate("MainWindow", "A"))
        self.label_6.setText(_translate("MainWindow", "Frame range:"))
        self.CheckButton.setText(_translate("MainWindow", "Check"))
        self.StopCheckButton.setText(_translate("MainWindow", "Stop"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Output File"))
        self.label_2.setText(_translate("MainWindow", "Output Folder:"))
        self.OutFolderButton.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "Option:"))
        self.Unchecked.setText(_translate("MainWindow", "Unchecked Output"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.StopOutButton.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
