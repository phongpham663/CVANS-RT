# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CameraConnectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraConnectDialog(object):
    def setupUi(self, CameraConnectDialog):
        CameraConnectDialog.setObjectName("CameraConnectDialog")
        CameraConnectDialog.resize(742, 490)
        CameraConnectDialog.setMinimumSize(QtCore.QSize(742, 490))
        CameraConnectDialog.setMaximumSize(QtCore.QSize(742, 490))
        self.layoutWidget = QtWidgets.QWidget(CameraConnectDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.deviceUrlRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.deviceUrlRadioButton.setObjectName("deviceUrlRadioButton")
        self.horizontalLayout_12.addWidget(self.deviceUrlRadioButton)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)
        self.deviceUrlEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.deviceUrlEdit.setEnabled(True)
        self.deviceUrlEdit.setObjectName("deviceUrlEdit")
        self.horizontalLayout_2.addWidget(self.deviceUrlEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.filenameRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.filenameRadioButton.setObjectName("filenameRadioButton")
        self.horizontalLayout_10.addWidget(self.filenameRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.importFilePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.importFilePushButton.setObjectName("importFilePushButton")
        self.horizontalLayout_10.addWidget(self.importFilePushButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.filenameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout_9.addWidget(self.filenameEdit)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 8, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 7, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordEdit.setMinimumSize(QtCore.QSize(90, 0))
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 9, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 4, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 2, 1, 1, 1)
        self.channelsEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.channelsEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.channelsEdit.setObjectName("channelsEdit")
        self.gridLayout.addWidget(self.channelsEdit, 2, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 5, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 6, 1, 1)
        self.ipEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ipEdit.setMinimumSize(QtCore.QSize(136, 0))
        self.ipEdit.setObjectName("ipEdit")
        self.gridLayout.addWidget(self.ipEdit, 2, 5, 1, 1)
        self.portEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.portEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.portEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.portEdit.setObjectName("portEdit")
        self.gridLayout.addWidget(self.portEdit, 2, 7, 1, 1)
        self.rtspRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.rtspRadioButton.setObjectName("rtspRadioButton")
        self.gridLayout.addWidget(self.rtspRadioButton, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.resWEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.resWEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resWEdit.setFont(font)
        self.resWEdit.setObjectName("resWEdit")
        self.horizontalLayout_14.addWidget(self.resWEdit)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.resHEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.resHEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resHEdit.setFont(font)
        self.resHEdit.setObjectName("resHEdit")
        self.horizontalLayout_14.addWidget(self.resHEdit)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.apiPreferenceComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.apiPreferenceComboBox.setObjectName("apiPreferenceComboBox")
        self.horizontalLayout_6.addWidget(self.apiPreferenceComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.imageBufferSizeEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.imageBufferSizeEdit.setFont(font)
        self.imageBufferSizeEdit.setObjectName("imageBufferSizeEdit")
        self.horizontalLayout.addWidget(self.imageBufferSizeEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.dropFrameCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dropFrameCheckBox.setFont(font)
        self.dropFrameCheckBox.setObjectName("dropFrameCheckBox")
        self.verticalLayout_3.addWidget(self.dropFrameCheckBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.capturePrioComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.capturePrioComboBox.setFont(font)
        self.capturePrioComboBox.setObjectName("capturePrioComboBox")
        self.verticalLayout_2.addWidget(self.capturePrioComboBox)
        self.processingPrioComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.processingPrioComboBox.setFont(font)
        self.processingPrioComboBox.setObjectName("processingPrioComboBox")
        self.verticalLayout_2.addWidget(self.processingPrioComboBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.tabLabelEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabLabelEdit.setFont(font)
        self.tabLabelEdit.setObjectName("tabLabelEdit")
        self.horizontalLayout_5.addWidget(self.tabLabelEdit)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.enableFrameProcessingCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enableFrameProcessingCheckBox.setFont(font)
        self.enableFrameProcessingCheckBox.setObjectName("enableFrameProcessingCheckBox")
        self.horizontalLayout_7.addWidget(self.enableFrameProcessingCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.resetToDefaultsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resetToDefaultsPushButton.setObjectName("resetToDefaultsPushButton")
        self.horizontalLayout_4.addWidget(self.resetToDefaultsPushButton)
        self.okCancelBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.okCancelBox.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelBox.setObjectName("okCancelBox")
        self.horizontalLayout_4.addWidget(self.okCancelBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CameraConnectDialog)
        self.okCancelBox.accepted.connect(CameraConnectDialog.accept)
        self.okCancelBox.rejected.connect(CameraConnectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CameraConnectDialog)
        CameraConnectDialog.setTabOrder(self.deviceUrlRadioButton, self.deviceUrlEdit)
        CameraConnectDialog.setTabOrder(self.deviceUrlEdit, self.filenameEdit)
        CameraConnectDialog.setTabOrder(self.filenameEdit, self.rtspRadioButton)
        CameraConnectDialog.setTabOrder(self.rtspRadioButton, self.usernameEdit)
        CameraConnectDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        CameraConnectDialog.setTabOrder(self.passwordEdit, self.ipEdit)
        CameraConnectDialog.setTabOrder(self.ipEdit, self.portEdit)
        CameraConnectDialog.setTabOrder(self.portEdit, self.channelsEdit)
        CameraConnectDialog.setTabOrder(self.channelsEdit, self.resWEdit)
        CameraConnectDialog.setTabOrder(self.resWEdit, self.resHEdit)
        CameraConnectDialog.setTabOrder(self.resHEdit, self.apiPreferenceComboBox)
        CameraConnectDialog.setTabOrder(self.apiPreferenceComboBox, self.imageBufferSizeEdit)
        CameraConnectDialog.setTabOrder(self.imageBufferSizeEdit, self.dropFrameCheckBox)
        CameraConnectDialog.setTabOrder(self.dropFrameCheckBox, self.capturePrioComboBox)
        CameraConnectDialog.setTabOrder(self.capturePrioComboBox, self.processingPrioComboBox)
        CameraConnectDialog.setTabOrder(self.processingPrioComboBox, self.tabLabelEdit)
        CameraConnectDialog.setTabOrder(self.tabLabelEdit, self.enableFrameProcessingCheckBox)
        CameraConnectDialog.setTabOrder(self.enableFrameProcessingCheckBox, self.resetToDefaultsPushButton)

    def retranslateUi(self, CameraConnectDialog):
        _translate = QtCore.QCoreApplication.translate
        CameraConnectDialog.setWindowTitle(_translate("CameraConnectDialog", "Connect to Camera"))
        self.label_1.setText(_translate("CameraConnectDialog", "Camera:"))
        self.deviceUrlRadioButton.setText(_translate("CameraConnectDialog", "Device url:"))
        self.label_10.setText(_translate("CameraConnectDialog", "[0, 1, 2, ...]"))
        self.filenameRadioButton.setText(_translate("CameraConnectDialog", "From file:"))
        self.importFilePushButton.setText(_translate("CameraConnectDialog", "Import"))
        self.label_19.setText(_translate("CameraConnectDialog", ":"))
        self.label_21.setText(_translate("CameraConnectDialog", "/Streaming/Channels/"))
        self.label_15.setText(_translate("CameraConnectDialog", "password"))
        self.label_23.setText(_translate("CameraConnectDialog", "rtsp://"))
        self.label_18.setText(_translate("CameraConnectDialog", "port"))
        self.label_17.setText(_translate("CameraConnectDialog", "Channels"))
        self.label_20.setText(_translate("CameraConnectDialog", "@"))
        self.label_14.setText(_translate("CameraConnectDialog", "username"))
        self.label_16.setText(_translate("CameraConnectDialog", "ip address"))
        self.label_24.setText(_translate("CameraConnectDialog", ":"))
        self.rtspRadioButton.setText(_translate("CameraConnectDialog", "RTSP:"))
        self.label_11.setText(_translate("CameraConnectDialog", "Resolution (W x H):"))
        self.label_12.setText(_translate("CameraConnectDialog", "[optional]"))
        self.label_13.setText(_translate("CameraConnectDialog", "x"))
        self.label.setText(_translate("CameraConnectDialog", "apiPreference:"))
        self.label_3.setText(_translate("CameraConnectDialog", "Image Buffer:"))
        self.label_2.setText(_translate("CameraConnectDialog", "Size (number of images/frames):"))
        self.label_4.setText(_translate("CameraConnectDialog", "[1-999]"))
        self.dropFrameCheckBox.setText(_translate("CameraConnectDialog", "Drop frame if image buffer is full"))
        self.label_5.setText(_translate("CameraConnectDialog", "Thread Priorities:"))
        self.label_6.setText(_translate("CameraConnectDialog", "Capture Thread:"))
        self.label_7.setText(_translate("CameraConnectDialog", "Processing Thread:"))
        self.label_8.setText(_translate("CameraConnectDialog", "Tab Label:"))
        self.enableFrameProcessingCheckBox.setText(_translate("CameraConnectDialog", "Enable frame processing"))
        self.resetToDefaultsPushButton.setText(_translate("CameraConnectDialog", "Reset to Defaults"))

