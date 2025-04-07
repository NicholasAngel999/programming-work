#films 
#makeup 
#barbie!
#surfing (only a few)
#sneak some climbing in there 
#maybe some funny questions about me 


#img_path = "./ducks wallpaper.png"

#img = cv2.imread(img_path)
#print(img)
#cv2.imshow("test", img)
#cv2.waitKey(0)


import time
import sys
import cv2


def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i, end="...\n", flush=True)
        time.sleep(1)


score = 0


