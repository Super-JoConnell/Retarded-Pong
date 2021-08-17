# Retarded-Pong
A Retarded Version of Pong Coded in Python using turtle module (not pygame)

run "Game Of Pong.py" directly to play (Requires Python + dependency (playsound))
if require to compile then see below

Music Produced by Myself as well I'm not great at it just threw something together quickly

w, s, up and down control the paddles 
Escape to quit game


i created this as part of my learning towards python
next game will be pygame orientated 

dependencies: python + playsound (google how to install python)

to install playsound (once you have python):

pip install playsound

or

pip3 install playsound



to compile in windows recommend:
pyinstaller

to install:

pip install pyinstaller

or

pip3 install pyinstaller

then 

pyinstaller --noconfirm --onefile --console --icon "Icon.ico"  "Game Of Pong-nomusic.py" 

notes: when compiled the music and sfx clash and the program crashes, so i recommend to compile the sfx version only which is this command
