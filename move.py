import os

# Basic Operations
# Function to get file extension
def getName(filepath):
    return os.path.basename(filepath)

# Function to get file name
def getExt(filepath):
    return os.path.splitext(filepath)[1][1:]

def getDir(filepath):
    return os.path.dirname(filepath)


def decideAndMoveFile(filename, groups):
    subDir = decideDir(filename, groups)
    if subDir == "ignore":
        return
    moveFile(filename, subDir)


# Decide in which directory file needs to be moved after considering config groups
def decideDir(filename, groups):
    fExt = getExt(filename)
    for groupDict in groups:
        for (group, items) in groupDict.items():
            if fExt in items:
                fExt = group
    return fExt

# Function to Move File
def moveFile(filename, subDir):
    fName = getName(filename)
    fDir = getDir(filename)

    if (fName[0] != "."):
        if not os.path.exists(os.path.join(fDir, subDir)):
            os.mkdir(os.path.join(fDir, subDir))

        os.rename(filename, os.path.join(fDir, subDir, fName))
