import importlib.util
import subprocess
import sys
from src.CSharpSocket import *

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    CSharpSocket().Trace(package + " package has succesfully installed!")


def CheckIfPackagesIsInstalled(importName, installationName):
    isPackageExist = importlib.util.find_spec(importName)
    if isPackageExist is None:
        CSharpSocket().Trace("Installing " + importName )
        install(installationName)
        return False
    return True

def InstallMissingPackages():
    try:
        IsPackageMissingList = []
        IsPackageMissingList.append(CheckIfPackagesIsInstalled("win32", "pywin32"))
        IsPackageMissingList.append(CheckIfPackagesIsInstalled("pyautogui", "PyAutoGUI"))
        IsPackageMissingList.append(CheckIfPackagesIsInstalled("pywinauto", "pywinauto"))
        IsPackageMissingList.append(CheckIfPackagesIsInstalled("cv2", "opencv-python"))
        IsPackageMissingList.append(CheckIfPackagesIsInstalled("PIL", "Pillow"))

        if any(x == False for x in IsPackageMissingList):
            CSharpSocket().Trace("Re-Run Process to apply missing pip packages.")
            sleep(1)
            CSharpSocket().Trace("Disconnected")
            sys.exit()

    except Exception as e:
        raise ValueError(str(e))