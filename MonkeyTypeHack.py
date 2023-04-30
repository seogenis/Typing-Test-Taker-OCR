#Note: This project was made to type at superhuman speeds on monkeytype.com

# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
import pyautogui
import cv2
from PIL import ImageGrab
import pytesseract
import keyboard
import time

# Path of tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\seanw\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#time before execution
time.sleep(3)



def row1():
    #row 1
    cap = ImageGrab.grab(bbox =(90,316,1231,352))
    row1 = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
    print(row1)
    pyautogui.write(row1)
    pyautogui.write(" ")

def row2():
    #row 2
    cap = ImageGrab.grab(bbox =(90,356,1233,392))
    row2 = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
    print(row2)
    pyautogui.write(row2)
    pyautogui.write(" ")


def loop():
    t_end = time.time() + 30
    while(time.time() < t_end):
        #breaks loop when press esc key
        if keyboard.is_pressed('0'):
            break

        #current 2nd row
        cap = ImageGrab.grab(bbox =(90,356,1233,392))
        row = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
        print(row)
        pyautogui.write(row)
        pyautogui.write(" ")
        
        #pyautogui.write(text)
        time.sleep(0.2)

row1()
row2()
loop()
