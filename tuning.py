# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tuningui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TuningUI(object):
    def setupUi(self, TuningUI):
        TuningUI.setObjectName("TuningUI")
        TuningUI.setWindowModality(QtCore.Qt.WindowModal)
        TuningUI.setEnabled(True)
        TuningUI.resize(1080, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TuningUI.sizePolicy().hasHeightForWidth())
        TuningUI.setSizePolicy(sizePolicy)
        TuningUI.setMinimumSize(QtCore.QSize(1080, 800))
        TuningUI.setMaximumSize(QtCore.QSize(1080, 800))
        TuningUI.setAcceptDrops(False)
        self.frame = QtWidgets.QFrame(TuningUI)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(80, 20, 521, 611))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 570, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 570, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 131, 431))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 180, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 210, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 250, 101, 20))
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 300, 111, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 370, 110, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 570, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 80, 141, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 140, 91, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 180, 81, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 100, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 80, 171, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 60, 91, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 140, 111, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 170, 111, 41))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 570, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 320, 131, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_9.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 570, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 10, 421, 21))
        self.label_12.setObjectName("label_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(180, 320, 181, 191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 40, 41, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(120, 60, 31, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 80, 40, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 47, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 120, 150, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 47, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 160, 150, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.frame_2 = QtWidgets.QFrame(TuningUI)
        self.frame_2.setGeometry(QtCore.QRect(600, 20, 461, 611))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 560, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 560, 75, 23))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 80, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.graphicsView = PlotWidget(self.frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(30, 150, 461, 371))
        self.graphicsView.setObjectName("graphicsView")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(186, 120, 131, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 560, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(270, 80, 61, 21))
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(TuningUI)
        self.frame_3.setGeometry(QtCore.QRect(580, 650, 211, 110))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(50, 40, 151, 30))
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(50, 80, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(170, 80, 47, 20))
        self.label_15.setObjectName("label_15")
        self.frame_4 = QtWidgets.QFrame(TuningUI)
        self.frame_4.setGeometry(QtCore.QRect(100, 650, 461, 111))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(350, 10, 47, 13))
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(410, 10, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.radioButton_15 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_15.setGeometry(QtCore.QRect(30, 10, 171, 17))
        self.radioButton_15.setObjectName("radioButton_15")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_12.setGeometry(QtCore.QRect(190, 70, 101, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 70, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.IP_Info = QtWidgets.QFrame(TuningUI)
        self.IP_Info.setGeometry(QtCore.QRect(850, 640, 161, 181))
        self.IP_Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IP_Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IP_Info.setObjectName("IP_Info")

        self.retranslateUi(TuningUI)
        QtCore.QMetaObject.connectSlotsByName(TuningUI)

    def retranslateUi(self, TuningUI):
        _translate = QtCore.QCoreApplication.translate
        TuningUI.setWindowTitle(_translate("TuningUI", "Form"))
        self.pushButton_2.setText(_translate("TuningUI", "Generate"))
        self.pushButton.setText(_translate("TuningUI", "Quit"))
        self.groupBox.setTitle(_translate("TuningUI", "Frequency PreDef"))
        self.radioButton.setText(_translate("TuningUI", "SF 10Khz"))
        self.radioButton_2.setText(_translate("TuningUI", "SF 20KHZ"))
        self.radioButton_3.setText(_translate("TuningUI", "SF 30Khz"))
        self.radioButton_4.setText(_translate("TuningUI", "SF 40Khz"))
        self.radioButton_5.setText(_translate("TuningUI", "SF 50Khz"))
        self.radioButton_6.setText(_translate("TuningUI", "Other"))
        self.label.setText(_translate("TuningUI", "Sampling Freq"))
        self.lineEdit.setText(_translate("TuningUI", "10"))
        self.pushButton_8.setText(_translate("TuningUI", "SF Update"))
        self.pushButton_9.setText(_translate("TuningUI", "SF Reset"))
        self.pushButton_3.setText(_translate("TuningUI", "Flash"))
        self.groupBox_2.setTitle(_translate("TuningUI", "HW Feature"))
        self.checkBox_2.setText(_translate("TuningUI", "UART Enable"))
        self.checkBox_4.setText(_translate("TuningUI", "Debug Enable"))
        self.checkBox_5.setText(_translate("TuningUI", "USB Enable"))
        self.checkBox_3.setText(_translate("TuningUI", "I2C Enable"))
        self.groupBox_3.setTitle(_translate("TuningUI", "Appl Feature"))
        self.checkBox_7.setText(_translate("TuningUI", "Wave Fitting"))
        self.checkBox_8.setText(_translate("TuningUI", "Active Noise Cancellation"))
        self.checkBox_9.setText(_translate("TuningUI", "Adaptive Sampling"))
        self.checkBox.setText(_translate("TuningUI", "Enable Noise Mix"))
        self.pushButton_6.setText(_translate("TuningUI", "Start"))
        self.groupBox_4.setTitle(_translate("TuningUI", "FFT SIZE"))
        self.radioButton_7.setText(_translate("TuningUI", "1024"))
        self.radioButton_8.setText(_translate("TuningUI", "2048"))
        self.radioButton_9.setText(_translate("TuningUI", "4096"))
        self.pushButton_7.setText(_translate("TuningUI", "Compile"))
        self.label_12.setText(_translate("TuningUI", "Tunable Parameters"))
        self.groupBox_5.setTitle(_translate("TuningUI", "IP Information"))
        self.label_5.setText(_translate("TuningUI", "Board IP addr"))
        self.label_6.setText(_translate("TuningUI", "PORT"))
        self.lineEdit_4.setText(_translate("TuningUI", "7"))
        self.lineEdit_3.setText(_translate("TuningUI", "192.168.0.10"))
        self.lineEdit_9.setText(_translate("TuningUI", "192.168.0.11"))
        self.label_11.setText(_translate("TuningUI", "PORT"))
        self.lineEdit_10.setText(_translate("TuningUI", "7"))
        self.label_10.setText(_translate("TuningUI", "Dest IP addr"))
        self.label_8.setText(_translate("TuningUI", "IP Mask"))
        self.lineEdit_7.setText(_translate("TuningUI", "255.255.255.0"))
        self.label_9.setText(_translate("TuningUI", "Gateway"))
        self.lineEdit_8.setText(_translate("TuningUI", "192.168.0.1"))
        self.pushButton_4.setText(_translate("TuningUI", "Visualize"))
        self.pushButton_5.setText(_translate("TuningUI", "Stop"))
        self.label_2.setText(_translate("TuningUI", "Data Visualizer"))
        self.label_3.setText(_translate("TuningUI", "FFT Spectrum"))
        self.lineEdit_5.setText(_translate("TuningUI", "192.168.0.10"))
        self.label_4.setText(_translate("TuningUI", "Frequency resolution / bin"))
        self.pushButton_10.setText(_translate("TuningUI", "Capture"))
        self.label_7.setText(_translate("TuningUI", "Ip Address"))
        self.label_13.setText(_translate("TuningUI", "Debug Parameters"))
        self.label_14.setText(_translate("TuningUI", "Frequency of test waveform"))
        self.label_15.setText(_translate("TuningUI", "Khz"))
        self.pushButton_11.setText(_translate("TuningUI", "SW Reset"))
        self.label_16.setText(_translate("TuningUI", "Status"))
        self.radioButton_15.setText(_translate("TuningUI", "In Application Programming"))
        self.pushButton_12.setText(_translate("TuningUI", "Go to Boot Mode"))
        self.pushButton_13.setText(_translate("TuningUI", "Flash"))

from pyqtgraph import PlotWidget
