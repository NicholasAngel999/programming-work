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

score = 0

type_text("Hey baby, ive made you a quiz about all sorts of things from films and makeup to me and surfing")


