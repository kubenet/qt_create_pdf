# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(531, 222, 201, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 10, 181, 171))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 191, 211))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 17, 181, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 10, 341, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 321, 117))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 160, 321, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 230, 511, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ????????????????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "??????????????????"))
        self.radioButton.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.radioButton_2.setText(_translate("MainWindow", "?????????????????? ????????????"))
        self.radioButton_3.setText(_translate("MainWindow", "?????????????????? ????????????"))
        self.checkBox_3.setText(_translate("MainWindow", "???????? ???????????? ?? ??????????????????"))
        self.checkBox.setText(_translate("MainWindow", "?????????????????? ?? PDF"))
        self.checkBox_2.setText(_translate("MainWindow", "?????????????????? PDF ?? ???????? ????????"))
        self.checkBox_4.setText(_translate("MainWindow", "?????????????????? ?? ?????????????? Word"))
        self.groupBox_2.setTitle(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????? ??????"))
        self.pushButton.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.label_5.setText(_translate("MainWindow", "???????? ????????????"))
        self.label_3.setText(_translate("MainWindow", "????????????"))
        self.label_4.setText(_translate("MainWindow", "??????????????????"))
        self.label_7.setText(_translate("MainWindow", "??????????"))
        self.pushButton_2.setText(_translate("MainWindow", "1. ?????????????? ?? Word"))
        self.pushButton_4.setText(_translate("MainWindow", "2. ?????????????? ?? PDF"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????????: Word ?? PDF"))
        self.menu.setTitle(_translate("MainWindow", "&??????????????"))
        self.menu_2.setTitle(_translate("MainWindow", "&????????"))