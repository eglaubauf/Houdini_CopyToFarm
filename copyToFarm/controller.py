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

class Controller(QtWidgets.QMainWindow, view.Ui_copyFarm):

    def __init__(self, parent = hou.qt.mainWindow()):
        super(Controller, self).__init__(parent)
        
        self.setupUi(self)
        #Set Houdini Style to Window
        self.setProperty("houdiniStyle", True)
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

    #Fill Text Fields with Data
    def initFields(self):
        self.ws_line.setText(self.core.ws)
        self.updateLinkedFiles()
   
    #Update Linked Files in List
    def updateLinkedFiles(self):
        files = self.core.getAllLinkedFiles()
        model = QtGui.QStandardItemModel()
        self.files_lst.setModel(model)
        for parm, f in files:
            item = QtGui.QStandardItem(f)
            model.appendRow(item)

    # #Set Destintation by User
    def setDestination(self):
        userDest = hou.ui.selectFile(title='Choose a Destination', file_type=hou.fileType.Directory)
        if userDest is not None:
            self.core.setDestination(userDest)
            self.dest_btn.setText(self.core.dest)
    
    #Set User Preferences    
    def setCopyAll(self):
        self.core.setCopyAll(True)
    
    #Set User Preferences 
    def setCopyNew(self):
        self.core.setCopyAll(False)

    #Execute Copying of Files
    def execute(self):
        #Check if Destination has been set correctly
        if self.core.dest is '':
            hou.ui.displayMessage('Please set a destination first', buttons=('Ok',))
            return
        count = self.core.copyFiles()
        if count == 0:
            hou.ui.displayMessage('An error occured during copying - Please Check your Source and Destination Paths', buttons=('Ok',))
            return
        message = str(count) + ' Files copied succesfully'
        hou.ui.displayMessage(message, buttons=('Ok',))
        
        self.destroy()







