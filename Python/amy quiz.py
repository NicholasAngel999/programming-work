#films 
#makeup 
#barbie!
#surfing (only a few)
#sneak some climbing in there 
#maybe some funny questions about me 

import time
import sys

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
type_text("are you ready baby")
while True:
    countdown(3)
    type_text('''Hey baby, ive made you a quiz about all sorts of things from "
    films and makeup to me and surfing''')
    q14 = input()
    if q14 == "yes":
        print(320)
        break
    else:
        print(420)
        break



