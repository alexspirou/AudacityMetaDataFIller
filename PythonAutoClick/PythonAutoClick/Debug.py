
import subprocess
from src.Dependencies import InstallMissingPackages
from src.HelperFunctions import *
InstallMissingPackages()
import sys

def PressTabAndWrite(msg, times, delay):
    for i in range(0, times):
        pyautogui.press('tab')

    pyautogui.typewrite(msg)
    sleep(delay)

def RunProcess():
    
     try:
        
        #args = ["ena-ewfew , duo-feew", "tria-ewfew", "tessera-fewfew", "pente-fwefew", "eksi", "efta", "oxtw", "enia","deka"]

        args = (sys.argv)
        counter = 0
        for i in args:
           args[counter] = i.replace("-", " " )
           CSharpSocket().Trace(i)
           counter +=1

        FindAndClick(r"Media\minimize.PNG",retries=0,timeoutSec=10, conf =0.8, delay=0.1)
        FindAndClick(r"Media\audacityAppOpen.PNG",retries=0,timeoutSec=10, conf =0.8,delay=0.1)
        sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 'E')

        #FindAndClick(r"Media\wavMicrosoft.PNG",retries=1,timeoutSec=10, conf=0.7, delay=0.1)
        #FindAndClick(r"Media\mp3Files.PNG",retries=1,timeoutSec=10, conf=0.7, delay=0.1)
        FindAndClick(r"Media\renameClick.PNG",retries=0,timeoutSec=10, conf=0.7, delay=0.1)

        pyautogui.hotkey('ctrl', 'a')
        sleep(0.1)
        pyautogui.press('delete')
        songName = args[1] + " " + args[2]
        pyautogui.typewrite(songName)
        sleep(0.1)

        try:
           FindAndClick(r"Media\save.PNG",retries=1,timeoutSec=10, conf=0.7, delay=0.1)
        except Exception as e:
           CSharpSocket().Trace(e)
    
        tabDelay = 0.1

        FindAndClick(r"Media\ArtistName.PNG",retries=1,timeoutSec=10,conf=0.7, delay=0.1)
        pyautogui.typewrite(args[1])



        for i in range(2, 8):
            PressTabAndWrite(args[i], 2, tabDelay)

        #pyautogui.typewrite(args[1])
        #FindAndClick(r"Media\TrackTitle.PNG",retries=1,timeoutSec=10,conf=0.7,delay=0.2)
        #pyautogui.typewrite(args[2])
        ##FindAndClick(r"Media\AlbumTitle.PNG",retries=1,timeoutSec=10,conf=0.7,delay=0.2)
        ##pyautogui.typewrite(args[3])
        #pyautogui.press('tab')
        #sleep(0.3)
        #pyautogui.press('tab') 
        #sleep(0.3)
        #FindAndClick(r"Media\TrackNumber.PNG",retries=1,timeoutSec=10,conf=0.7)
        #pyautogui.typewrite(args[4])
        #FindAndClick(r"Media\Year.PNG",retries=1,timeoutSec=10,conf=0.7,delay=0.2)
        #pyautogui.typewrite(args[5])
        #FindAndClick(r"Media\Genre.PNG",retries=0,timeoutSec=10,conf=0.7,delay=0.2)
        #pyautogui.typewrite(args[6])
        #FindAndClick(r"Media\Comments.PNG",retries=0,timeoutSec=10,conf=0.7,delay=0.2)
        #pyautogui.typewrite(args[7])

        FindAndClick(r"Media\Ok.PNG",retries=0,timeoutSec=10,conf=0.7,delay=0.2)


        CSharpSocket().Trace("Hello5")
     except Exception as e:
         CSharpSocket().Trace("Operation : "+ FailedMsgConst)
         CSharpSocket().Trace("Hello5")
         sleep(3)
         raise ValueError(str(e))


try:
     RunProcess()
except Exception as e:
    CSharpSocket().Trace(e)
    sleep(5)
    sys.exit()
