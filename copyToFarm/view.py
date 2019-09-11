# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_copyFarm(object):
    def setupUi(self, copyFarm):
        copyFarm.setObjectName("copyFarm")
        copyFarm.resize(589, 510)
        self.verticalLayoutWidget = QtWidgets.QWidget(copyFarm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 561, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 10, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Top_lbl.setObjectName("Top_lbl")
        self.verticalLayout.addWidget(self.Top_lbl)
        self.ws_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ws_line.setEnabled(True)
        self.ws_line.setAcceptDrops(False)
        self.ws_line.setReadOnly(True)
        self.ws_line.setObjectName("ws_line")
        self.verticalLayout.addWidget(self.ws_line)
        self.target_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.target_lbl.setObjectName("target_lbl")
        self.verticalLayout.addWidget(self.target_lbl)
        self.dest_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dest_btn.setObjectName("dest_btn")
        self.verticalLayout.addWidget(self.dest_btn)
        self.files_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.files_lbl.setObjectName("files_lbl")
        self.verticalLayout.addWidget(self.files_lbl)
        self.files_lst = QtWidgets.QListView(self.verticalLayoutWidget)
        self.files_lst.setObjectName("files_lst")
        self.verticalLayout.addWidget(self.files_lst)
        self.import_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.import_btn.setObjectName("import_btn")
        self.verticalLayout.addWidget(self.import_btn)
        self.copyAll_rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.copyAll_rbtn.setChecked(True)
        self.copyAll_rbtn.setObjectName("copyAll_rbtn")
        self.verticalLayout.addWidget(self.copyAll_rbtn)
        self.copyNew_rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.copyNew_rbtn.setObjectName("copyNew_rbtn")
        self.verticalLayout.addWidget(self.copyNew_rbtn)
        self.openNew_Box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.openNew_Box.setObjectName("openNew_Box")
        self.verticalLayout.addWidget(self.openNew_Box)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(copyFarm)
        QtCore.QMetaObject.connectSlotsByName(copyFarm)

    def retranslateUi(self, copyFarm):
        _translate = QtCore.QCoreApplication.translate
        copyFarm.setWindowTitle(_translate("copyFarm", "CopyToFarm"))
        self.Top_lbl.setText(_translate("copyFarm", "Current Workspace:"))
        self.target_lbl.setText(_translate("copyFarm", "Target Workspace:"))
        self.dest_btn.setText(_translate("copyFarm", "Choose Destination Project Directory"))
        self.files_lbl.setText(_translate("copyFarm", "Files to Copy"))
        self.import_btn.setText(_translate("copyFarm", "ImportReferences (also saves the current File as *_imported)"))
        self.copyAll_rbtn.setText(_translate("copyFarm", "Copy Everything"))
        self.copyNew_rbtn.setText(_translate("copyFarm", "Copy Newer Files only"))
        self.openNew_Box.setText(_translate("copyFarm", "Open File in New Location"))
