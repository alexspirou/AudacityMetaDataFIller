
from ctypes import windll
import sys
from src.Dependencies import InstallMissingPackages
InstallMissingPackages()

from time import sleep
sleep(0.5) # Wait until command's executed from application
from src.CSharpSocket import *


try:
    CSharpSocket().Trace("Mp3 save data has stared", 0.5)

    windll.user32.BlockInput(True)
    CSharpSocket().Trace("Inputs are disabled. Press Ctrl+Alt+Delete to activate them in case they are needed.", 0.5)
    try:
        pass
    except:
        pass
    CSharpSocket().Trace("Rework has finished")
    sleep(1)
    CSharpSocket().Trace("Disconnected")
    windll.user32.BlockInput(False)
    sys.exit()

except Exception as e:
    CSharpSocket().TraceError(str(e))
    sys.exit()
