[![CodeQL](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml)
<div>
    <iframe src="https://discord.com/widget?id=967250293190434907&theme=dark" 
        width="350" 
        height="500" 
        allowtransparency="true" 
        frameborder="0" 
        sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts">
    </iframe>
</div>
# Lost Ark Anti AFK Bot:
To tackle the issue of long queue times and harsh AFK timers I have created an Anti AFK Bot For Lost ARK

# Feature Set:
- Automatic Screen Resolution Detection (Changes Bot Click Area To Your Resolution!)
- Allows you to change the default click list of buttons to randomise your session!
- Allows you to set shortest/longest amount of time bot randomises between!
- Queue Detection and Auto Character Launch - Supported Resolutions:
```
1920x1080
2560x1080
2560x1440
3440x1440
3840x1600
```
- Queue Detection - Languages Supported For Queue Detection: 
```
English
German
French
Italian
Turkish
Danish
```

# Want To Help The Project?
- Currently Queue Detection only has a few supported resolutions. What I need is gathered user data from all screen resolutions.
- Firstly download and setup https://github.com/mjdarby/ScreenCoordinateHelper
- Next record the exact cords for the "Waiting for server/queue" Box and record these details as follow:
```
randomxbot = play area bottom x
randomxtop = play area top x
randomybot = play area bottom y
randomytop = play area top y
launchx = character launch button x
launchy = character launch button y
scleft = Waiting Box Top Left (x value)
sctop = Waiting Box Top Left (y value)
scwidth = Waiting Box Width (work this out with x cords for left and right of the box)
scheight = Waiting Box Height (work this out with y cords for top and bottom of the box)
```
- For incorporation into the main branch I expect you to play around with your settings in the python program!
- You should amend the settings for your resolution until you have a working Queue Detection in place!
- Lastly raise a GitHub issue with your screen resolution and the above details!

# Latest Release:
- Currently [V2.7](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V2.7) is the latest release available!
- Update Queue Detection for more support on resolutions
- Changed the way screen resolutions get supported into the main program branch (requires user testing so I can just push release!)

## Setup:
1) Firstly Install Python and make sure to install the package manager PIP (Do This In Admin Privileges in CMD etc)
2) Copy and paste the commands below into your terminal. This will install the Open Source packages needed to run the program.
```
pip install pyautogui
pip install tesseract
pip install pytesseract
```
3) Make Sure To Install Either 64bit or 32bit for your machine: [Tesseract Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki)
4) Make sure the path for the above installation is saved to this location or program will not work ('C:/Users/"YOURUSER"/AppData/Local/Programs/Tesseract-OCR/tesseract.exe')
5) Now move the program into another drive preferably from the game and rename it to you choosing (bury this in a few random files)
6) Enjoy usage!

# Usage:
## Usage ~ About:
- I recommend using the obfuscated version of the project nicknamed "Obfuscated.py"
- This is the fastest and most secure version of the program always
- You should use this program in a private location only accessible to you such as the Memory Chamber ideally
- You can change the name of the program and put it anywhere inside your file system to hide it further.
## Usage ~ Program Setup:
- System automatically detects resolution and adjusts config accordingly
- System asks you if you want to add more Buttons to the Click List
- You can choose to expand out the default buttons which are: ['q','w','e','r','a','s','d','f']
- System asks you to enter shortest/longest wait time to randomly select wait times between
- System then asks you if you want to run Queue Detection (Use this if you are in a Queue, Currently Supported Resolution 1920x1080 - May work on others!)
- If you do run Queue Detection it will continuously keep checking the screen to see if you are in a Queue every 10 seconds!
- Make sure nothing blocks the Lost Ark "Waiting for Server" box otherwise the program will think you are out of the Queue!
## Usage ~ Program Run time:
- The system starts off with a mouse click at a random screen location cords within the clickable area of the game
- The system then presses a key which is randomly selected from the Buttons List (Either Default Or Custom)
- The system executes between mouse clicks and button presses between your random selected time frame
- The systems selects a random screen coordinate to click every time
- The system selects a random key button every time of the array of "usable" buttons
- The program runs indefinitely until closed and be careful not to run the program e.g. just on your desktop

# Release History:
- [V2.7](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V2.7) (Major Release(Patch))
- [V2.6](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V2.6) (Major Release(Patch))
- [V2.5](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V2.5) (Major Release(Patch))
- Check [Releases](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases) To See All Old History of V1.0 to V2.4

## Plans for the future:
- Wait for feedback of Queue detection and resolve any issues and add more resolution support!
- Playing around with windows notifications and discord hooks!
- Possibly turning into a UI based program or offering both!

## About:
- Built this program for a friend and the program currently is fully undetected and ready to go
- You can use any version of the program as they are all the same always!
- You are free to use this code in your own projects and tamper with it as much as you like! If you make any cool changes let me know and I will merge it to main branch!
- You can also run your own Obfuscation on the source code to better hide the program if you do worry about EAC (Easy Anti Cheat)
- Currently Macros have no definite answer on bans etc but generic rules state anything that is a bot or left unattended is breaking the rules
- You are responsible for the usage of the program and anything that happens to your account is on you

