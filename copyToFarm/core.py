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

import os
import hou
import fastCopy as fc

class Core():

    def __init__(self):
        self.ws = self.getWorkspace()
        self.files = []
        self.copyAll = True
        self.dest = ''
        self.destinationHip = ''
        self.OpenNew = False
        self.ImportFlag = False

    # # Query the Current Workspace (Hip File directory)
    def getWorkspace(self):  
        return hou.hipFile.path()[:-len(hou.hipFile.basename())] 
    
    # Gets a List of all Files in a Maya Scene
    def getAllLinkedFiles(self):
        self.files = hou.fileReferences()
        return self.files

    # Set the New Destination
    def setDestination(self, newDest):            
        self.dest = newDest
        return True

    #Set all Files to Copy
    def setCopyAll(self, flag):
        self.copyAll = flag

    #Set to Copy only newer Files
    def setOpenNew(self, flag):
        self.OpenNew = flag

    #Set to Copy only newer Files
    def setImport(self, flag):
        self.importFlag = flag

    #Copies all Files to a new Workspace
    def copyFiles(self):
        
        count = 0
        #Save File first
        self.saveFile()

        #Now Copy all references
        for parm, f in self.files:
            
            f = hou.expandString(f)
            occur = f.rfind("/")
            #Full Paths from SourceFile
            sourceFile = f[occur+1:]
            sourcePath = f[:occur+1]
            sourcePathSub = ''

            #Trim away Project Directory
            if sourcePath.startswith(self.ws) is True:
                sourcePathSub = sourcePath[len(self.ws):]
            else:
                occur = sourcePath.find('/')
                sourcePathSub = sourcePath[occur:]
            sourcePathSub = sourcePathSub.strip('/')
              

            # create Directories if Missing
            destinationPath = self.dest + sourcePathSub
            if not os.path.exists(destinationPath):
                try:
                    os.makedirs(destinationPath)
                except WindowsError:
                    return 0
                    
            #Create CopyPath
            destination = destinationPath + '/' + sourceFile
            #Copy only Newer Files?
            if self.copyAll is False:
                if os.path.exists(destination):
                    if os.path.getctime(f) > os.path.getctime(destination) is True:
                        try:
                            fc.copyfile(f, destination)
                        except:
                            return 0
                        count += 1
            else: 
                try:
                    fc.copyfile(f, destination)
                except:
                    return 0
                count +=1
            
            destinationParm = "$HIP/" + sourcePathSub + '/' + sourceFile
            parm.set(destinationParm)
            count += 1

        #Copy our Hip File in as a last Step
        if self.saveHipFileToDest() == 0:
            return 0
        return count

    def saveHipFileToDest(self):
        # create our Target Directory if Missing - checked already, but for future usage of this scripts
        if not os.path.exists(self.dest):
            try:
                os.makedirs(self.dest)
            except WindowsError:
                return 0
           
        self.destinationHip = self.dest + hou.hipFile.basename()
        hou.hipFile.save(self.destinationHip)
        return 1
    
    # #Reopens The File in the New Workspace
    def reOpenFile(self):
        hou.hipFile.load(self.destinationHip, suppress_save_prompt=True)

    # #Save Current File
    def saveFile(self):
        hou.hipFile.save()

 

            
            





