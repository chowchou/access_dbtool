# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 600)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("I.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 301, 411))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 281, 381))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 100, 211, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 60, 141, 31))
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 90, 141, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 120, 141, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 150, 141, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 480, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(19, 20, 531, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 30, 91, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 281, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 480, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox_t_0 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_0.setGeometry(QtCore.QRect(20, 530, 41, 16))
        self.checkBox_t_0.setObjectName("checkBox_t_0")
        self.checkBox_t_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_1.setGeometry(QtCore.QRect(70, 530, 41, 16))
        self.checkBox_t_1.setObjectName("checkBox_t_1")
        self.checkBox_t_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_2.setGeometry(QtCore.QRect(130, 530, 41, 16))
        self.checkBox_t_2.setObjectName("checkBox_t_2")
        self.checkBox_t_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_3.setGeometry(QtCore.QRect(190, 530, 41, 16))
        self.checkBox_t_3.setObjectName("checkBox_t_3")
        self.checkBox_t_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_4.setGeometry(QtCore.QRect(250, 530, 41, 16))
        self.checkBox_t_4.setObjectName("checkBox_t_4")
        self.checkBox_t_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_5.setGeometry(QtCore.QRect(310, 530, 41, 16))
        self.checkBox_t_5.setObjectName("checkBox_t_5")
        self.checkBox_t_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_6.setGeometry(QtCore.QRect(20, 550, 41, 16))
        self.checkBox_t_6.setObjectName("checkBox_t_6")
        self.checkBox_t_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_7.setGeometry(QtCore.QRect(70, 550, 41, 16))
        self.checkBox_t_7.setObjectName("checkBox_t_7")
        self.checkBox_t_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_8.setGeometry(QtCore.QRect(130, 550, 41, 16))
        self.checkBox_t_8.setObjectName("checkBox_t_8")
        self.checkBox_t_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_9.setGeometry(QtCore.QRect(190, 550, 41, 16))
        self.checkBox_t_9.setObjectName("checkBox_t_9")
        self.checkBox_t_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t_10.setGeometry(QtCore.QRect(250, 550, 41, 16))
        self.checkBox_t_10.setObjectName("checkBox_t_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Check_Access"))
        self.groupBox.setTitle(_translate("MainWindow", "检测日志"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "检测项"))
        self.checkBox_1.setText(_translate("MainWindow", "字段值一致性检测"))
        self.checkBox_2.setText(_translate("MainWindow", "材质检测"))
        self.checkBox_3.setText(_translate("MainWindow", "非法字符检测"))
        self.checkBox_4.setText(_translate("MainWindow", "管块孔数检测"))
        self.checkBox_5.setText(_translate("MainWindow", "附属物埋深一致性检测"))
        self.pushButton_2.setText(_translate("MainWindow", "开始检测"))
        self.groupBox_3.setTitle(_translate("MainWindow", "数据库路径"))
        self.pushButton_3.setText(_translate("MainWindow", "选择数据库"))
        self.label.setText(_translate("MainWindow", "当前数据库路径："))
        self.label_2.setText(_translate("MainWindow", "C:UserslenovoDesktopoffice2010Office14"))
        self.pushButton_4.setText(_translate("MainWindow", "清空日志"))
        self.checkBox_t_0.setText(_translate("MainWindow", "FS"))
        self.checkBox_t_1.setText(_translate("MainWindow", "GD"))
        self.checkBox_t_2.setText(_translate("MainWindow", "JK"))
        self.checkBox_t_3.setText(_translate("MainWindow", "LD"))
        self.checkBox_t_4.setText(_translate("MainWindow", "RS"))
        self.checkBox_t_5.setText(_translate("MainWindow", "SS"))
        self.checkBox_t_6.setText(_translate("MainWindow", "TR"))
        self.checkBox_t_7.setText(_translate("MainWindow", "TX"))
        self.checkBox_t_8.setText(_translate("MainWindow", "WS"))
        self.checkBox_t_9.setText(_translate("MainWindow", "YS"))
        self.checkBox_t_10.setText(_translate("MainWindow", "ZS"))