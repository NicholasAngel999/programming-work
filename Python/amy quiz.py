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
        
from rapidfuzz import fuzz

def is_correct(user_input, valid_answers, threshold=80):
    user_input = user_input.lower().strip()
    for ans in valid_answers:
        if fuzz.ratio(user_input, ans.lower().strip()) >= threshold:
            return True
    return False

score = 0


