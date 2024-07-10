### Vet Sci Dog Auscultation App
* Built in Python 3.12.4
* Setup Python Libs
  * tkinter 
  * pygame 
  * bleak 
  * may need "sudo apt install libsdl1.2-dev" "sudo apt install libsdl-mixer1.2-dev" for pygame if you get an import error for libsdl



### 02/07/2024
* v1 of DogAusc local application
  * built using PAGE gui builder, with basic model and controller
  * next steps are implementing file loading and media playback
  * Build the "Begin Auscultation" command, a 60s loop that constantly listens for input from the arduino and plays the appropriate sound.
  * Build the "End Auscultation" command, which will simply stop the loop.
* Do we want to be able to change each sensor's track individually? Can change audio test buttons to specific audio load.
* Problem - if we want to load 4 audio files from one directory, the files have to be named a certain way for the system to differentiate between sensor 1-4 audio.


### 03/07/2024
* touchup on asynchronous methods
* tried porting into an EXE, pyinstaller is missing the bleak lib modules
* idk how fix
* still need to implement file loading and naming solution
* exe needs to be signed for security

### 04/07/2024
* moved v1 code to its own folder
* start v2 using customtkinter
* Change load files button to use a popup window and set each sensor audio
* implement file loading 
* implement async BLE connection again (dunno how to work with ctk)

### 04/07/2024
* received updated BLE code
* integrated popup and custom file loading for app and model
* need to do presets, shouldnt be too hard
