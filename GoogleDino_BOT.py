from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

replayBtn = (480, 303)
dinosaur = (190, 312)
 
def restartGame():
     pyautogui.click(replayBtn)
    
def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    
c = 70
b = 110
d = 1

def main():
     global c
     global b
     global d 
   

     while True:
          box = (dinosaur[0] + c,dinosaur[1],dinosaur[0] + b,dinosaur[1] + 33)
          image = ImageGrab.grab(box)
          grayImage = ImageOps.grayscale(image)
          a = array(grayImage.getcolors())
          ac = a.sum()
          if (ac>=1576):
               pyautogui.keyDown('space')
               pyautogui.keyUp('space')
          if (ac == 1320 and d==1):
                    c=c+32
                    print(c)
                    d=2
                    b=b+32

              
restartGame()          
main()






