import sys
import os
import datetime
import signal 
import shutil
import subprocess

from ctypes import *
from src.CSharpSocket import *

import pywinauto 
import pyautogui

from threading import Thread
import functools
from time import *

SucceedMsgConst = "SUCCEED"
FailedMsgConst = "FAILED"
def MoveAndClick(path, delay, conf):
        X, Y = pyautogui.locateCenterOnScreen(path, confidence = conf)
        pyautogui.moveTo(X, Y, delay)
        pyautogui.leftClick()
        return X,Y

def MoveAndRightClick(path, delay, conf):
        X, Y = pyautogui.locateCenterOnScreen(path, confidence = conf)
        pyautogui.moveTo(X, Y, delay)
        pyautogui.click(button=2)
        return X,Y

def IsSpecificDialogShown(path, conf):
    try:
        X, Y = pyautogui.locateCenterOnScreen(path, confidence = conf)
        print(X,Y)
        return True
    except Exception as e:
        return False

def FindAndClick(path, delay = 0.5, conf = 0.7, retries = 1,timeoutSec = 15):
    timeout = time() + timeoutSec 
    retryCounter = 0
    traceCounter = 0
    x, y = 0,0
    while(x == 0 and y == 0):
        try:
            x, y = MoveAndClick(path, delay, conf)
            return x,y
        except Exception as e:
            if(traceCounter == 0):
                CSharpSocket().Trace("[SEARCHING]"+path)

            if(time() > timeout and retryCounter == retries):
                raise ValueError("[NOT FOUND]" + path )
            # Timeout
            if(time() > timeout and retryCounter < retries):
                timeout = time() + timeoutSec
                retryCounter += 1
                CSharpSocket().Trace("[NOT FOUND RETRY]" + path)
                pyautogui.moveTo(500, 500, 1)
                if(retryCounter==1):
                    conf -= 0.2

            traceCounter = 1
    CSharpSocket().Trace("[FOUND]"+path)


def FindAndRightClick(path, delay = 0.5, conf = 0.7, retries = 1,timeoutSec = 15):
    timeout = time() + timeoutSec 
    retryCounter = 0
    traceCounter = 0
    x, y = 0,0
    while(x == 0 and y == 0):
        sleep(0.5)
        try:
            x, y = MoveAndRightClick(path, delay, conf)
            return x,y
        except Exception as e:
            if(traceCounter == 0):
                CSharpSocket().Trace("[SEARCHING]"+path)

            if(time() > timeout and retryCounter == retries):
                raise ValueError("[NOT FOUND]" + path )
            # Timeout
            if(time() > timeout):
                timeout = time() + timeoutSec
                retryCounter += 1
                CSharpSocket().Trace("[NOT FOUND RETRY]" + path)
                pyautogui.moveTo(500, 500, 1)
                if(retryCounter==1):
                    conf -= 0.2
           
            traceCounter = 1
    CSharpSocket().Trace("[FOUND]"+path)      

def WaitUntilFindSnip1orSnip2ToClick(path1, path2 ,delay = 0.5, conf = 0.7):
    x, y = 0,0
    while(x == 0 and y == 0):
        try:
            x, y = MoveAndClick(path1, delay, conf)
            return x,y
        except Exception as e:
            try:
                x, y = MoveAndClick(path2, delay, conf)
                return x,y
            except Exception as e:
                CSharpSocket().Trace("[SEARCHING]"+path2)
            CSharpSocket().Trace("[FOUND]"+path1)

def WaitUntilDialogShown(path, conf =0.7, retries = 1,timeOutSec = 60):
    timeout = time() + timeOutSec 
    traceCounter = 0
    retryCounter = 0
    isDialogOpen = False
    # First try
    while(not isDialogOpen):
        isDialogOpen = IsSpecificDialogShown(path,conf)
        if(traceCounter == 0):
            CSharpSocket().Trace("[SEARCHING]"+path)
            traceCounter = 1
        # Break
        if(time() > timeout and retryCounter == retries):
            raise ValueError("[NOT FOUND]"+ path)
        # Retry
        if(time() > timeout):
            timeout = time() + timeOutSec
            retryCounter+=1
            pyautogui.moveTo(500, 500, 1) and pyautogui.moveTo(800, 500, 1) and pyautogui.moveTo(500, 800, 1)
            if(retryCounter == 1):
                conf = conf - 0.2 
            CSharpSocket().Trace("[NOT FOUND RETRY]" + path)
 
    CSharpSocket().Trace("[FOUND]"+path)      

def WaitUntilDialogShownAndClick(path, conf=0.7, retryTimes = 1,timeoutSec = 60):
    timeout = time() + timeoutSec
    retryCounter = 0
    traceCounter = 0
    isDialogOpen = False
    while(not isDialogOpen):
        isDialogOpen = IsSpecificDialogShown(path,conf)
        if(traceCounter == 0):
            CSharpSocket().Trace( "[FOUND]"+path)
            traceCounter = 1
         # Retry
        if(time() > timeout and retryCounter == 0):
            timeout = time() + timeoutSec
            retryCounter = 1
            pyautogui.moveTo(500, 500, 1) and pyautogui.moveTo(800, 500, 1) and pyautogui.moveTo(500, 800, 1)
            conf = conf - 0.2
            CSharpSocket().Trace("[NOT FOUND RETRY]" + path)
        # Break
        if(time() > timeout and retryCounter == retryTimes):
            raise ValueError("[NOT FOUND]"+ path)
    
    pyautogui.click()
    CSharpSocket().Trace("[FOUND]"+path)     

def CloseWindow(x, y):
    pyautogui.moveTo(x, y, 0.3)
    pyautogui.click()
    pyautogui.hotkey('alt', 'f4')

def OpenExe(path):
    app = pywinauto.Application(backend="uia").start(path)
    app.window()

def IsApplicationAlreadyInstalled(installationFolderPath, appName):
    if os.path.exists(installationFolderPath):
        CSharpSocket().Trace(appName + AlreadyMsgConst)
        sleep(0.1)
        return True
    return False

def CopyInstallerToLocalFolder(localUser, destinationFolder, srcFile, installerName):
    desktopPath = localUser + "\\" + destinationFolder
    shutil.copy(srcFile, desktopPath)
    newPath = desktopPath + installerName
    return newPath

def CopyFileToFolder(srcFile, destinationFolder):
    shutil.copy(srcFile, destinationFolder)

def WriteToText(message, filePath = r"C:\Users\Log.txt"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filePath, 'a') as f:
        f.write(message + ":::" + now + "\n")


def AppendTextInFirstLine(dest, content):
    with open(dest, "r+") as f: s = f.read(); f.seek(0); f.write(content + "\n" + s)
   
def AppendTextInLastLine(dest, content):
    with open(dest, 'a') as outfile:
        outfile.write(content+"\n")

def ReadDataFromFile(path):
    with open(path) as f:
        contents = f.read()
        return contents

def ReadRangeOfFile(filename, start, end):
    try:
        f=open(filename, "r")
        lines = f.readlines()
        f.close()
        lines = lines[start:end]
        return ListToString(lines)
    except Exception as e:
        raise ValueError("Counld not read range ", start, end, filename )
       
def ListToString(list):
    for row in list:
            string = ''.join(str(row) for row in list)
    return string


def TraceGivenPackages(args):
    try:
        packageCounter = 0
        packagesToInstall = ""
        for packages in args:
            if(packageCounter > 2): # Standard inputs from application
                if(packageCounter == 3): #One package
                    packagesToInstall = packages
                else:
                    packagesToInstall = packagesToInstall + ", " + packages
            packageCounter+=1
        CSharpSocket().Trace("Packages to be installed : " + packagesToInstall , 0.5)
    except Exception as e:
        raise ValueError(str(e))


