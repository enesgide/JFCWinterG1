### 02/07/2024
* v1 of DogAusc local application
  * built using PAGE gui builder, with basic model and controller
  * next steps are implementing file loading and media playback
  * Build the "Begin Auscultation" command, a 60s loop that constantly listens for input from the arduino and plays the appropriate sound.
  * Build the "End Auscultation" command, which will simply stop the loop.
* Do we want to be able to change each sensor's track individually? Can change audio test buttons to specific audio load.
* Problem - if we want to load 4 audio files from one directory, the files have to be named a certain way for the system to differentiate between sensor 1-4 audio.