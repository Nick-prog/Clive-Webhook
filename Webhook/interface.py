# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Enrollment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from Webhook.requests import entries, entries_Fee
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import Webhook
import time

class Thread(QtCore.QThread):
    def run(self):
        QtCore.QThread.sleep(10)

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(650, 480)
        Dialog.setStyleSheet("background-color: rgb(226, 226, 226);")
        Dialog.setWindowIcon(QIcon('Webhook-Images/TAMUK Logo 3.jpg'))
        Dialog.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

        #Beginning of "Upload Documents" tab
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 650, 480))
        self.tabWidget.setObjectName("tabWidget")
        self.Upload = QtWidgets.QWidget()
        self.Upload.setObjectName("Upload")
        self.Horizontal_Line = QtWidgets.QFrame(self.Upload)
        self.Horizontal_Line.setGeometry(QtCore.QRect(20, 350, 591, 20))
        self.Horizontal_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_Line.setObjectName("Horizontal_Line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Upload)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 210, 251, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Department = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Department.setObjectName("Department")
        self.verticalLayout.addWidget(self.Department)
        self.Dept_List = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Dept_List.setObjectName("Dept_List")

        for x in range (7):
            item = QtWidgets.QListWidgetItem()
            self.Dept_List.addItem(item)

        self.verticalLayout.addWidget(self.Dept_List)
        self.progressBar = QtWidgets.QProgressBar(self.Upload)
        self.progressBar.setGeometry(QtCore.QRect(40, 370, 571, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Pull = QtWidgets.QPushButton(self.Upload)
        self.Pull.setGeometry(QtCore.QRect(500, 410, 75, 23))
        self.Pull.setObjectName("Pull")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Upload)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 260, 301, 67))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Storage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Storage.setObjectName("Storage")
        self.verticalLayout_2.addWidget(self.Storage)
        self.Storage_Input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Storage_Input.setObjectName("Storage_Input")
        self.verticalLayout_2.addWidget(self.Storage_Input)
        self.Vertical_Line = QtWidgets.QFrame(self.Upload)
        self.Vertical_Line.setGeometry(QtCore.QRect(290, 60, 20, 281))
        self.Vertical_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vertical_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vertical_Line.setObjectName("Vertical_Line")
        self.Information = QtWidgets.QTextBrowser(self.Upload)
        self.Information.setGeometry(QtCore.QRect(20, 40, 271, 151))
        self.Information.setObjectName("Information")
        self.Real_Time = QtWidgets.QTableWidget(self.Upload)
        self.Real_Time.setGeometry(QtCore.QRect(320, 30, 301, 221))
        self.Real_Time.setMinimumSize(QtCore.QSize(155, 0))
        self.Real_Time.setStyleSheet("")
        self.Real_Time.setObjectName("Real_Time")
        self.Real_Time.setColumnCount(4)
        self.Real_Time.setRowCount(6)

        for y in range(6):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            item.setFont(font)
            self.Real_Time.setVerticalHeaderItem(y, item)

        for x in range(4):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            item.setFont(font)
            self.Real_Time.setHorizontalHeaderItem(x, item)

        for x in range(6):
            for y in range(4):
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setItalic(True)
                item.setFont(font)
                self.Real_Time.setItem(x, y, item)
                item.setFlags(Qt.ItemIsEditable)
            
        self.Storage_Current = QtWidgets.QLabel(self.Upload)
        self.Storage_Current.setGeometry(QtCore.QRect(40, 400, 331, 20))
        self.Storage_Current.setObjectName("Storage_Current")
        self.Dept_Current = QtWidgets.QLabel(self.Upload)
        self.Dept_Current.setGeometry(QtCore.QRect(40, 420, 331, 16))
        self.Dept_Current.setObjectName("Dept_Current")
        self.Refresh = QtWidgets.QPushButton(self.Upload)
        self.Refresh.setGeometry(QtCore.QRect(320, 30, 31, 31))
        self.Refresh.setIcon(QIcon('Webhook-Images/refresh-image.png'))
        self.Refresh.setText("")
        self.Refresh.setObjectName("Refresh")
        self.Current_Status = QtWidgets.QLabel(self.Upload)
        self.Current_Status.setGeometry(QtCore.QRect(580, 410, 120, 23))
        self.Current_Status.setObjectName("Current_Status")
        self.Current_Status.setText("Waiting...")
        self.Storage_Input.textChanged['QString'].connect(self.Storage_Current.setText)
        self.Dept_List.currentTextChanged['QString'].connect(self.Dept_Current.setText)
        self.thread = Thread()
        self.Pull.clicked.connect(self.on_click)
        self.thread.finished.connect(lambda: self.Pull.setEnabled(True))
        self.Refresh.clicked.connect(self.on_refresh)
        self.thread.finished.connect(lambda: self.Refresh.setEnabled(True))
        self.buttonReply = QtWidgets.QMessageBox(self.Upload)
        self.buttonReply.setFixedSize(200, 300)
        self.buttonReply.setObjectName("Confirmation Box")
        self.buttonReply.setText("Are you sure?")
        self.buttonReply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonReply.setWindowTitle("Confirmation")

        #Beginning of "Fee Waiver Request Tab"
        self.tabWidget.addTab(self.Upload, "")
        self.Fee = QtWidgets.QWidget()
        self.Fee.setObjectName("Fee")
        self.Storage_Current2 = QtWidgets.QLabel(self.Fee)
        self.Storage_Current2.setGeometry(QtCore.QRect(40, 400, 331, 20))
        self.Storage_Current2.setObjectName("Storage_Current2")
        self.Horizontal_Line = QtWidgets.QFrame(self.Fee)
        self.Horizontal_Line.setGeometry(QtCore.QRect(20, 350, 591, 20))
        self.Horizontal_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_Line.setObjectName("Horizontal_Line")
        self.progressBar2 = QtWidgets.QProgressBar(self.Fee)
        self.progressBar2.setGeometry(QtCore.QRect(40, 370, 571, 23))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setObjectName("progressBar2")
        self.Pull2 = QtWidgets.QPushButton(self.Fee)
        self.Pull2.setGeometry(QtCore.QRect(500, 410, 75, 23))
        self.Pull2.setObjectName("Pull2")
        self.Pull2.clicked.connect(self.on_click_2)
        self.thread.finished.connect(lambda: self.Pull2.setEnabled(True))
        self.Current_Status2 = QtWidgets.QLabel(self.Fee)
        self.Current_Status2.setGeometry(QtCore.QRect(580, 410, 120, 23))
        self.Current_Status2.setObjectName("Current_Status2")
        self.Current_Status2.setText("Waiting...")
        self.buttonReply2 = QtWidgets.QMessageBox(self.Fee)
        self.buttonReply2.setFixedSize(200, 300)
        self.buttonReply2.setObjectName("Confirmation Box")
        self.buttonReply2.setText("Are you sure?")
        self.buttonReply2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonReply2.setWindowTitle("Confirmation")
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.Fee)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(320, 260, 301, 67))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Storage2 = QtWidgets.QLabel(self.verticalLayoutWidget2)
        self.Storage2.setObjectName("Storage2")
        self.verticalLayout_2.addWidget(self.Storage2)
        self.Storage_Input2 = QtWidgets.QLineEdit(self.verticalLayoutWidget2)
        self.Storage_Input2.setObjectName("Storage_Input2")
        self.Storage_Input2.textChanged['QString'].connect(self.Storage_Current2.setText)
        self.verticalLayout_2.addWidget(self.Storage_Input2)
        self.Vertical_Line2 = QtWidgets.QFrame(self.Fee)
        self.Vertical_Line2.setGeometry(QtCore.QRect(290, 60, 20, 281))
        self.Vertical_Line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vertical_Line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vertical_Line2.setObjectName("Vertical_Line2")
        self.Information2 = QtWidgets.QTextBrowser(self.Fee)
        self.Information2.setGeometry(QtCore.QRect(20, 40, 271, 300))
        self.Information2.setObjectName("Information2")
        
        self.graphWidget = pg.PlotWidget(self.Fee)
        self.graphWidget.setGeometry(QtCore.QRect(320, 30, 301, 221))
        self.graphWidget.setBackground('w')
        self.Refresh2 = QtWidgets.QPushButton(self.Fee)
        self.Refresh2.setGeometry(QtCore.QRect(320, 30, 31, 31))
        self.Refresh2.setIcon(QIcon('Webhook-Images/refresh-image.png'))
        self.Refresh2.setText("")
        self.Refresh2.setObjectName("Refresh2")
        self.Refresh2.clicked.connect(self.on_refresh_2)
        self.thread.finished.connect(lambda: self.Refresh2.setEnabled(True))
        self.Entries = QtWidgets.QLabel(self.Fee)
        self.Entries.setGeometry(QtCore.QRect(320, 10, 331, 20))
        self.Entries.setObjectName("Entries")
        self.tabWidget.addTab(self.Fee, "")
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def on_click(self):
        self.buttonReply.setInformativeText("%s\n%s" %(self.Storage_Current.text(), self.Dept_Current.text()))
        if self.buttonReply.exec() == QMessageBox.Yes:
            if not self.thread.isRunning():
                self.Pull.setEnabled(False)
                self.Refresh.setEnabled(False)
                self.Current_Status.setText("Wating...")
                self.thread.start()
                location = self.Storage_Input.text()
                department = self.Dept_List.currentItem()
                for i in range(101):
                    time.sleep(0.05)
                    self.progressBar.setValue(i)
                self.progressBar.setValue(0)
                self.Current_Status.setText("Pulled!")
                Webhook.download(department.text(),location)
                Webhook.delete(department.text())
                self.Refresh.setEnabled(True)
        else:
            pass

    def on_refresh(self):
        if not self.thread.isRunning():
            self.Refresh.setEnabled(False)
            self.Pull.setEnabled(False)
            self.Current_Status.setText("Waiting...")
            for i in range(101):
                time.sleep(0.05)
                self.progressBar.setValue(i)
            self.thread.start()
            _translate = QtCore.QCoreApplication.translate
            for y in range(6):
                item = self.Real_Time.item(y, 0)
                item.setText(_translate("Dialog", Webhook.entries(y)))
                item = self.Real_Time.item(y, 1)
                item.setText(_translate("Dialog", Webhook.date(y)))
                item = self.Real_Time.item(y, 2)
                item.setText(_translate("Dialog", Webhook.current(y)))
                item = self.Real_Time.item(y, 3)
                item.setText(_translate("Dialog", Webhook.last()))
            self.progressBar.setValue(0)
            self.Current_Status.setText("Refreshed!")
            self.Pull.setEnabled(True)

    def on_click_2(self):
        self.buttonReply2.setInformativeText("%s\n" %(self.Storage_Current2.text()))
        if self.buttonReply2.exec() == QMessageBox.Yes:
            if not self.thread.isRunning():
                self.Pull2.setEnabled(False)
                self.Current_Status2.setText("Wating...")
                self.thread.start()
                location = self.Storage_Input2.text()
                for i in range(101):
                    time.sleep(0.05)
                    self.progressBar2.setValue(i)
                self.progressBar2.setValue(0)
                self.Current_Status2.setText("Pulled!")
                Webhook.download2(location)
                Webhook.delete_Fee()
        else:
            pass

    def on_refresh_2(self):
        hours = []
        entries = []
        if not self.thread.isRunning():
            self.Refresh2.setEnabled(False)
            self.Pull2.setEnabled(False)
            self.Current_Status2.setText("Waiting...")
            for i in range(101):
                time.sleep(0.05)
                self.progressBar2.setValue(i)
            self.thread.start()
            dict = Webhook.entries_date_fee()
            hours = [*dict]
            for x in hours:
                entries.append(dict[x])
            self.graphWidget.plot(hours, entries)
            self.progressBar2.setValue(0)
            self.Current_Status2.setText("Refreshed!")
            self.Entries.setText("Current Entries: %s" % Webhook.entries_Fee())
            self.Pull2.setEnabled(True)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clive Webhook"))
        self.Department.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Department?</span></p></body></html>"))
        self.Dept_List.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\"> This dialogue box is used to determine what department the user wishes to pull and store data from...</span></p></body></html>"))
        __sortingEnabled = self.Dept_List.isSortingEnabled()
        self.Dept_List.setSortingEnabled(False)

        for x in range(7):
            item = self.Dept_List.item(x)
            item.setText(_translate("Dialog", Webhook.departments(x)))

        self.Dept_List.setSortingEnabled(__sortingEnabled)
        self.Pull.setText(_translate("Dialog", "Pull"))
        self.verticalLayoutWidget.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Storage Location?</span></p></body></html>"))
        self.Storage_Input.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage_Input.setText(_translate("Dialog", "//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s" %(Webhook.month_year(), Webhook.now())))

        self.Pull2.setText(_translate("Dialog", "Pull"))
        self.verticalLayoutWidget2.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage2.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Storage Location?</span></p></body></html>"))
        self.Storage_Input2.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\">  This dialogue box specifies the location the user wishes to store the downloaded files... </span>(Ex: C:/Users/KUNRR004/Desktop)</p></body></html>"))
        self.Storage_Input2.setText(_translate("Dialog", "//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s" %(Webhook.month_year(), Webhook.now())))

        self.Information.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The table located on the top right will display helpful information based on the traffic received by the webhook. Each row displays a number that indicates a department (Ex: &quot;Admisison&quot;= &quot;-1-&quot;, &quot;Financial Aid&quot; = &quot;-2-&quot;, etc.). For each column, information on the current amount of entries per department, the date and time of the last entry, as well as the last time the system updated will be displayed.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- How do you use this program?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To fully utilize this program, the user must specify what department they wish to focus on along with a location on their PC to store the downloaded documents. Once done, the user can veiw two labels below the progress bar to confirm their selections before clicking the &quot;Pull&quot; button to activate the process. The progress bar will then progressively fill up to indicate when the process is finished.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"left\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Disclaimer:</span> <span style=\" font-style:italic;\">This program will pull only 100 entries at a time and will delete everything upon completion.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Version %s</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Links</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GitHub - https://github.com/Nick-prog/Clive-Webhook</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pipedream - https://pipedream.com/sources/dc_RWuzvge</p></body></html>") % Webhook.__version__)
        self.Real_Time.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.Real_Time.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Tip:</span><span style=\" font-style:italic;\"> The information shown displays the current up-to-date values of the total entries for the &quot;Upload Documents&quot; form, as well as, the last time the data was pulled.</span></p></body></html>"))

        for y in range(6):
            item = self.Real_Time.verticalHeaderItem(y)
            item.setText(_translate("Dialog", Webhook.table_vertical(y)))

        for x in range(4):
            item = self.Real_Time.horizontalHeaderItem(x)
            item.setText(_translate("Dialog", Webhook.table_horizontal(x)))

        __sortingEnabled = self.Real_Time.isSortingEnabled()
        self.Real_Time.setSortingEnabled(False)
        self.Real_Time.setSortingEnabled(__sortingEnabled)
        self.Storage_Current.setText(_translate("Dialog", "<html><head/><body><p>//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s</p></body></html>" % (Webhook.month_year(), Webhook.now())))
        self.Dept_Current.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic;\">Department?</span></p></body></html>"))
        self.Storage_Current2.setText(_translate("Dialog", "<html><head/><body><p>//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s</p></body></html>" % (Webhook.month_year(), Webhook.now())))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Upload), _translate("Dialog", "Upload Documents"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fee), _translate("Dialog", "Fee Waiver Request"))
        self.Entries.setText(_translate("Dialog", "<html><head/><body><p>Current Entries: (Refresh to find out!)</p></body></html>"))

        self.Information2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The table located on the top right will display real-time information based on the recent traffic for this clive form. The vertical numbers represent the current amount of entries based on the horizontal numbers representing the current time. For simplicity, a label can be located above the line graph that will display the current amount of entries available to pull. Click the refresh button to begin.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- How do you use this program?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To fully utilize this program, the user must specify what location they wish to download and store their documents to. Once done, the user can veiw the label below the progress bar to confirm their selections before clicking the &quot;Pull&quot; button to activate the process. The progress bar will then progressively fill up to indicate when the process is finished.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"left\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Disclaimer:</span> <span style=\" font-style:italic;\">This program will pull only 100 entries at a time and will delete everything upon completion. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Version %s</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Links</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GitHub - https://github.com/Nick-prog/Clive-Webhook</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pipedream - https://pipedream.com/sources/dc_nvuDJ8N</p></body></html>") % Webhook.__version__)
