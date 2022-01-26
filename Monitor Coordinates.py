import pyautogui as pag 
from PIL import ImageGrab 
import keyboard

print("기본: 0,0 ~ (1920,1080)=>(1919,1079)")
print("---사용법---")
print("측정: Alt ")
print("made by Ksh")
print("=")
a=0
while a==0:
    if keyboard.is_pressed('Alt'): #측정
        x, y = pag.position()
        print((x,y))
    if keyboard.is_pressed('F4'): #종료
        print()
        print("----종료 made by Ksh---")
        a=0
        break 
