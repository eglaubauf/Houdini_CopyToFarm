# Houdini_CopyToFarm

## Development stopped
This plugin will not be developed any further


This script provides a window in which the user is able to select a directory to copy the current file and it´s dependencies to a different, arbitrary location (e.g. a network storage). In this process the script will copy all linked/referenced files to the chosen location as long as they are below the current workspace. 

The addon also provides the user with a list of files which will be copied. The script is optmized for fast copying and copies only the files which are referenced or linked to within Houdini.

The user can also choose if only newer files or all files should be copied. In both cases existing files will be overwritten. The script will automatically open the new file in it´s new location. The old file will be left untouched.

This script has been tested with Houdini 17.5.360 and Windows 10. 

![alt text](https://raw.githubusercontent.com/eglaubauf/Houdini_CopyToFarm/master/images/Ui.png "The Provided UI by the Script")

## Features
- Copy Files to different Location (Links included)
- Import all References (and create a backup from it)
- List all Linked files
- Only copy newer files
- Copy all Files
- Open New File in one Step (also sets the Workspace to this new Location)
- Copy Files from any Location to new Project Directory (Rebuilds FolderStructure Below the new Project Location)
- works with Houdini 17.5.360 ( and older possibly as well but untested)
- OS-Exceptions are handled
- Windows only (at the Moment)


## Todos

- A possible Version for Linux/OSX (low Priority)

## Installation

1. Download zip or clone repo
2. Add the following Code to your 123.py or 456.py File which is located at '*UserDir*\houdini17.5\scripts' (Create it if you need to)

```
import sys 
sys.path.append("<Path to Your Downloaded Folder>\Houdini_CopyToFarm") 
```

3. Add provided Shelf or add Lines below to a shelf button:

```
import copyToFarm.controller as copyFarmCtrl
reload(copyFarmCtrl)
copyFarmCtrl.open()
```

### Contact/Issues/Features/Questions

If you find any bugs, have suggestions or anything else please contact me via Twitter or per Mail. Please check out my other Repos as well, they might be handy to you. For any questions and/or improvement suggestions just contact me via twitter or mail.<br>
Twitter: @eglaubauf <br>
Web: www.elmar-glaubauf.at
