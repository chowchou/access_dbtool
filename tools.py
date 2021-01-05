import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from main import Ui_MainWindow
from check import Check
import log


class Main_ui(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.button_click)
        self.clear_init()
        self.pushButton_2.clicked.connect(self.start_work)
        self.pushButton_4.clicked.connect(self.clear_log)
        self.setFixedSize(self.width(), self.height())

    def clear_init(self):
        self.label_2.clear()
        for i in range(1,6):
            sss = 'self.checkBox_%s.setChecked(True)' %str(i)
            eval(sss)

    def button_click(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        self.label_2.setText(directory[0])

    def printf(self,data):
        log.logging.info(str(data))
        self.textEdit.append(str(data))

    def printf_e(self,data):
        log.logging.info(str(data))
        data ='<font color=\"#ff2121\">' + str(data) +'</font>'
        self.textEdit.append(data)
    def printf_p(self,data):
        log.logging.info(str(data))
        data ='<font color=\"#228B22\">' + str(data) +'</font>'
        self.textEdit.append(data)


    def clear_log(self):
        self.textEdit.clear()

    def check_res(self,data):
        flag = data.get('flag')
        message = data.get('mes')
        id = data.get('id')
        if flag == '0':
            self.printf(message)
        if flag == '1':
            self.printf(message)
            # self.printf('-'*50)
        if flag == '3':
            self.printf_e(message)
            self.printf_e(id)
        if flag == '2':
            self.printf_p(message)
        if flag == '4':
            abs = '-'*23 + id + '-'*23
            self.printf_e(abs)


    def start_work(self):
        url = self.label_2.text()
        check_dict = {'url': url}
        for i in range(1,6):
            key = 'box_' + str(i)
            sss = 'self.checkBox_%s.isChecked()' %str(i)
            values = eval(sss)
            check_dict[key] = values
        check_types = {}
        for i in range(11):
            key = 'type_' + str(i)
            sss = 'self.checkBox_t_%s.isChecked()' % str(i)
            values = eval(sss)
            check_types[key] = values
        for i in check_types.values():
            if i:
                check_flag = True
                # return flag
                break
            else:
                check_flag = False

        if url and check_flag:
            # self.printf('运行')
            self.check_thread = Check(check_dict,check_types)
            self.check_thread._signal.connect(self.check_res)
            self.check_thread.start()
        else:
            self.printf('选择数据库!选择类别')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Main_ui()
    a.show()
    sys.exit(app.exec_())