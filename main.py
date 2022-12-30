import mouse
import keyboard
import time
#required library: sudo pip install mouse
#how to use library https://www.thepythoncode.com/article/control-mouse-python

#### NOTE : The mouse.click() function needs root access, so play button may not work in vscode
#### Use this if play button doesnt work: sudo python nameOfFile.py

DEBUG = True

if DEBUG:
    while True:
        #Press CTRL+C to exit DEBUGGING (Used to find coordinates on screen)
        print(f'moveMouse{str(mouse.get_position())}')
        time.sleep(4)


