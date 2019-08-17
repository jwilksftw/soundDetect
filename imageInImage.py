import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import pyscreenshot as ImageGrab
import time
import pyaudio
import wave
from array import array
import keyboard
import mouse
import time
import random
from pyclick import HumanClicker

time.sleep(2)
hc = HumanClicker()
def bobberfish():
        b=0
        for c in range(300, 850, 70):
            b+=1
            #Grabs the whole screen to search for 'Fishing Bobber' Tooltip
            im=ImageGrab.grab(bbox=(0,0,2560,1440))
            im.save('im'+str(b)+'.png')
            # Image we want to search
            img_rgb = cv.imread('im'+str(b)+'.png')
            # Make image grey to remove some variation
            img_grey = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            # Image we want to find
            template = cv.imread('cog2.png',0)
            # Match grey image to template
            w, h = template.shape[::-1]
            res = cv.matchTemplate(img_grey,template,cv.TM_CCOEFF_NORMED)
            
            # Set rules for what counts as a match
            threshold = 0.8
            loc = np.where( res >= threshold)
            
            # Draw red box around the item we think matches and starts listening for fish sound
            for pt in zip(*loc[::-1]):
                #Fish sound listen
                FORMAT=pyaudio.paInt16
                CHANNELS=2
                RATE=random.randint(2000, 5000)
                CHUNK=1024
                RECORD_SECONDS=1500
                FILE_NAME="RECORDING.wav"
                audio=pyaudio.PyAudio() #instantiate the pyaudio
                
                #recording prerequisites
                stream=audio.open(format=FORMAT,channels=CHANNELS, 
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)
                
                #starting recording
                frames=[]
                for i in range(0,100):
                    data=stream.read(CHUNK)
                    data_chunk=array('h',data)
                    vol=max(data_chunk)
                    #Volume threshold for fish sound. Might need to play around with it. Make sure system audio is used, NOT  a microphone. Turn off ambient sound.
                    if(vol>=1500):
                        print("something said")
                        #Autoloot
                        keyboard.press('shift')
                        mouse.click(button='right')
                        keyboard.release('shift')
                        return                    
                    else:
                        print("nothing")
                        #print(i)
                        if i==100:
                            return

            #Moves if the bobber hasn't been found
            hc.move((1310, c),.2)

while True:
    #Set '1' key to cast fishing
    hc.move((random.randint(1500, 1700), random.randint(500, 700)),.4)
    hc.move((random.randint(1500, 1700), random.randint(200, 300)),.4)
    keyboard.press_and_release('1')
    bobberfish()
    time.sleep(5)
    
        









