import time
import pyautogui
import pytesseract
import os
user = os.environ.get('USERNAME')
tesseractpath = 'C:/Users/' + user + '/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = tesseractpath
from random import randint

def ScreenSetup():
    res = pyautogui.size()
    if str(res) == "Size(width=640, height=480)":
        print("Using 640x480, Setting Randomx and Randomy")
        randomxbot = 286
        randomxtop = 351
        randomybot = 135
        randomytop = 301
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=1280, height=720)":
        print("Using 1280x720, Setting Randomx and Randomy")
        randomxbot = 573
        randomxtop = 702
        randomybot = 271
        randomytop = 602
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=1920, height=1080)":
        print("Using 1920x1080, Setting Randomx and Randomy")
        randomxbot = 382
        randomxtop = 1582
        randomybot = 181
        randomytop = 903
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=2560, height=1440)":
        print("Using 2560x1440, Setting Randomx and Randomy")
        randomxbot = 496
        randomxtop = 2056
        randomybot = 235
        randomytop = 1173
        launchx = 1135
        launchy = 1350
        scleft = 1030
        sctop = 609
        scwidth = 496
        scheight = 220
    elif str(res) == "Size(width=2560, height=1080)":
        print("Using 2560x1440, Setting Randomx and Randomy")
        randomxbot = 500
        randomxtop = 2100
        randomybot = 181
        randomytop = 903
        launchx = 1135
        launchy = 1350
        scleft = 1030
        sctop = 609
        scwidth = 496
        scheight = 220
    elif str(res) == "Size(width=2048, height=1080)":
        print("Using 2048x1080, Setting Randomx and Randomy")
        randomxbot = 404
        randomxtop = 1676
        randomybot = 191
        randomytop = 957
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=3440, height=1440)":
        print("Using 3440x1440, Setting Randomx and Randomy")
        randomxbot = 500
        randomxtop = 2900
        randomybot = 220
        randomytop = 1173
        launchx = 1720
        launchy = 716
        scleft = 1468
        sctop = 609
        scwidth = 400
        scheight = 300
    elif str(res) == "Size(width=3840, height=2160)":
        print("Using 3840x2160, Setting Randomx and Randomy")
        randomxbot = 572
        randomxtop = 3084
        randomybot = 286
        randomytop = 1759
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=3840, height=1600)":
        print("Using 3840x1600, Setting Randomx and Randomy")
        randomxbot = 590
        randomxtop = 3320
        randomybot = 260
        randomytop = 1350
        launchx = 1760
        launchy = 1500
        scleft = 1642
        sctop = 676
        scwidth = 552
        scheight = 246
    elif str(res) == "Size(width=5120, height=1440)":
        print("Using 5120x1440, Setting Randomx and Randomy")
        randomxbot = 744
        randomxtop = 4009
        randomybot = 220
        randomytop = 1173
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    elif str(res) == "Size(width=7680, height=4320)":
        print("Using 7680x4320, Setting Randomx and Randomy")
        randomxbot = 1488
        randomxtop = 6168
        randomybot = 572
        randomytop = 3518
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    else:
        print("Using Non-Supported Res, Changing Randomx and Randomy to Default Location!")
        print("Please raise an issue on GitHub with your screen res for future custom support!")
        randomxbot = 382
        randomxtop = 1582
        randomybot = 181
        randomytop = 903
        launchx = 855
        launchy = 1014
        scleft = 771
        sctop = 435
        scwidth = 373
        scheight = 204
    return randomxbot,randomxtop,randomybot,randomytop,launchx,launchy,scleft,sctop,scwidth,scheight

def TimeSetup():
    print("Usage Just Type an Integer e.g. 30")
    while True:
        try:
            timebot = int(input("Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): "))
            if timebot <= 0:
                print("Must Type an Integer > 0")
            elif timebot >= 4294967:
                print("This is to large of a time input!")
            else:
                timetop = int(input("Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): "))
                if timetop <= 0:
                    print("Must Type an Integer > 0")
                elif timetop <= timebot:
                    print("This should be not equal to or larger then the lowest amount in range")
                elif timetop >= 4294967:
                    print("This is to large of a time input!")
                else:
                    break
        except ValueError:
            print("Invalid Entry: Usage Just Type an Integer e.g. 30")
    return timebot,timetop

def RandomTimeGen(userTimeSettings):
        userSelected = userTimeSettings
        randtime = randint(userSelected[0], userSelected[1])
        return randtime

def TimeSleep(timeSleepSettings):
        userTimeSettings = timeSleepSettings
        timeWait = RandomTimeGen(userTimeSettings)
        print("Next Interaction Time: " + str(timeWait) + " second(s) or " + str(timeWait // 60) + " minute(s) (Integer Division Not Accurate Minute Representation)!")
        time.sleep(timeWait)

def RandomLocationGen(resScreenSize):
        screenSetup = resScreenSize
        randomx = randint(screenSetup[0],screenSetup[1])
        randomy = randint(screenSetup[2],screenSetup[3])
        return randomx,randomy

def MouseClick(retScreenSize):
    resScreenSize = retScreenSize
    randomlocval = RandomLocationGen(resScreenSize)
    randomx = randomlocval[0]
    randomy = randomlocval[1]
    pyautogui.moveTo(randomx,randomy)
    pyautogui.click()
    print("Mouse Clicked At: (" + str(randomx) + "," + str(randomy) + ")")

def ButtonSetup():
    ButtonClickList = ['q','w','e','r','a','s','d','f']
    print("The Default Button Click List Is:")
    print(ButtonClickList)
    while True:
        try:
            menuCheck = str(input("Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ")).lower()
            if menuCheck == "y":
                while True:
                    try:
                        amountToAppendCheck = int(input("How Many Keys Would You Like To Add To The List: "))
                        for i in range(amountToAppendCheck):
                            keyInput = input("Please Press a Key or Write The Key, Such As 'space' and then press enter: ")
                            ButtonClickList.append(keyInput)
                        break
                    except ValueError:
                        print("Type Error: You Have Entered An Incorrect Type! Please Enter An Integer")
                break
            elif menuCheck == "n":
                amountToAppendCheck = 0
                break
            else:
                print("Input Error: Please Enter Either Y or N")
        except ValueError:
            print("Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N")
    return ButtonClickList,amountToAppendCheck

def ButtonClick(buttonSetup):
    ButtonClickList = buttonSetup[0]
    ButtonClickTop = buttonSetup[1] + 7
    RandomButtonChoice = randint(0,ButtonClickTop)
    ButtonClick = ButtonClickList[RandomButtonChoice]
    pyautogui.press(ButtonClick)
    print("Button Clicked: " + ButtonClick)

def QueueDetection(retScreenSize):
    launchx = retScreenSize[4]
    launchy = retScreenSize[5]
    scleft = retScreenSize[6]
    sctop = retScreenSize[7]
    scwidth = retScreenSize[8]
    scheight = retScreenSize[9]
    while True:
        try:
            print("Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!")
            menuCheck = str(input("Would You Like To Start Queue Detection? Enter (Y) or (N): ")).lower()
            if menuCheck == "y":
                    try:
                        while True:
                            queueDetectionScreenshot = pyautogui.screenshot(region=(scleft,sctop,scwidth,scheight))
                            queueDetectionScreenshot.save(r"queueDetectionScreenshot.png")
                            path = 'queueDetectionScreenshot.png'
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Lost Ark Screen Being Analysed")
                            time.sleep(1)
                            queueDetect = pytesseract.image_to_string(Image.open(path))
                            if 'Waiting' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'Warten' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'Venter' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)                            
                            elif 'Attendre' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'In attesa' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9) 
                            elif 'Bekleme' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            else:
    
                                print("Out of Queue! :)")
                                print("Waiting 60 seconds to launch your character!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(60)
                                pyautogui.moveTo(launchx,launchy)
                                pyautogui.click()
                                print("Mouse Clicked At: (" + str(launchx) + "," + str(launchy) + ")")
                                print("Character Launch In Progress!")
                                print("30 Second Wait Time!")
                                time.sleep(30)
                                break
                        break
                    except ValueError:
                        print("Type Error: You Have Entered An Incorrect Type! Please Enter An Integer")
            elif menuCheck == "n":
                break
            else:
                print("Input Error: Please Enter Either Y or N")
        except ValueError:
            print("Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N")
    

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    retScreenSize = ScreenSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    buttonSetup = ButtonSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The Button Click List Is: ")
    print(buttonSetup[0])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    timeSleepSettings = TimeSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    QueueDetection(retScreenSize)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        TimeSleep(timeSleepSettings)  
        MouseClick(retScreenSize)
        TimeSleep(timeSleepSettings)
        ButtonClick(buttonSetup)
