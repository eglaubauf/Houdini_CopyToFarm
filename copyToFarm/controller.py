#####################################
#LICENSE                            #
#####################################
#
# Copyright (C) 2019  Elmar Glaubauf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


#import pymel.core as pm
#import maya.cmds as cmds
import hou 

from PySide2 import QtWidgets, QtCore, QtGui
#import maya.OpenMayaUI as omui
#from shiboken2 import wrapInstance

import copyToFarm.core as core
import copyToFarm.view as view

# Where is this script?
#SCRIPT_LOC = os.path.split(__file__)[0]

reload(core)
reload(view)
'''
Open with

import copyFarm.Controller as copyFarmCtrl
reload(copyFarmCtrl)
copyFarmCtrl.open()
    
'''

develop = True
tmpWindow = None
def open(develop = False):

    if develop:
        reload(core)
        reload(view)

    try:
        tmpWindow.close()
    except:
        pass

    tmpWindow = Controller()
    tmpWindow.show() 

# # wrapper to get mayas main window
# def getMayaMainWindow():
#     mayaPtr = omui.MQtUtil.mainWindow()
#     return wrapInstance(long(mayaPtr), QtWidgets.QWidget)

class Controller(QtWidgets.QMainWindow, view.Ui_copyFarm):

    def __init__(self, parent =  hou.ui.mainQtWindow()):
        super(Controller, self).__init__(parent)
        
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.core = core.Core()
        self.createConnections()
        self.initFields()

    # linking Buttons to Functions
    def createConnections(self):
        self.dest_btn.clicked.connect(self.setDestination)
        self.copyAll_rbtn.clicked.connect(self.setCopyAll)
        self.copyNew_rbtn.clicked.connect(self.setCopyNew)
        self.buttonBox.rejected.connect(self.destroy)
        self.buttonBox.accepted.connect(self.execute)
        self.openNew_Box.stateChanged.connect(self.openNewCheck)
        self.import_btn.clicked.connect(self.importReferences)   

    #Fill Text Fields with Data
    def initFields(self):
        return
        #self.ws_line.setText(self.core.ws)
        #self.updateLinkedFiles()
   
    #Update Linked Files in List
    def updateLinkedFiles(self):
        files = self.core.getAllLinkedFiles()
        model = QtGui.QStandardItemModel()
        self.files_lst.setModel(model)
        for f in files:
            item = QtGui.QStandardItem(f)
            model.appendRow(item)

    # #Set Destintation by User
    def setDestination(self):
        return
    #     # userDest = cmds.fileDialog2(fm=3)

    #     # if userDest is not None:
    #     #     self.core.setDestination(userDest[0])
    #     #     self.dest_btn.setText(self.core.dest)
    
    #Set User Preferences    
    def setCopyAll(self):
        self.core.setCopyAll(True)
    
    #Set User Preferences 
    def setCopyNew(self):
        self.core.setCopyAll(False)

    #Set User Preferences 
    def openNewCheck(self):
        self.core.setOpenNew(self.openNew_Box.isChecked())

    # #Import all References to current File
    def importReferences(self):
        return
    #     count = self.core.importReference()
    #     self.updateLinkedFiles()
    #     #Send Messages to User
    #     self.message(str(count) + 'References Imported Successfully')
    #     self.message('The File has been saved as ' + cmds.file(q=True, sn= True))

    # #Display a Message to the User
    # def message(self, msg):
    #     cmds.confirmDialog(m = msg, b='Okay')

    # #Execute Copying of Files
    def execute(self):
        return
    #     #Check if Destination has been set correctly
    #     if self.core.dest is '':
    #         cmds.confirmDialog(m='Please set a destination first', b='Okay')
    #         return
    #     count = self.core.copyFiles()
    #     if count == 0:
    #         message = 'An error occured during copying - Please Check your Destination Path'
    #         cmds.confirmDialog(m=message, b='Okay')
    #         return
    #     message = str(count) + ' Files copied succesfully'
    #     cmds.confirmDialog(m=message, b='Okay')
        
    #     if(self.core.OpenNew):
    #         self.core.setNewWorkspace()
    #         self.core.reOpenFile()
    #     self.destroy()







