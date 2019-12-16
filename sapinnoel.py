#My implementation of christmas tree for the unicorn hat
import unicornhat as UH
import datetime
import random
import time

print """Draw a christmas tree on the unicorn hat during 1.5h
                    *
                  * * *
                * * * * *
                  * * *
                * * * * *
              * * * * * * *
                    *
                    *
"""


UH.set_layout(UH.AUTO)
UH.rotation(270) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
UH.brightness(0.7)

tree =             [[3,0], \
              [2,1],[3,1],[4,1], \
        [1,2],[2,2],[3,2],[4,2],[5,2], \
              [2,3],[3,3],[4,3], \
        [1,4],[2,4],[3,4],[4,4],[5,4], \
  [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5], \
                    [3,6], \
                    [3,7]]

# Blink number of led based on the current day 
# On 25th, the whole tree will be blinking
balls_nbr = min(datetime.datetime.today().day, 25)
balls = random.sample(tree, balls_nbr)


#This will run during about 1.5h
it = 0
while it < 3600:
  for px in tree: 
    x, y = px
    if px in balls:
      r = random.randint(0, 255)
      g = random.randint(0, 255)
      b = random.randint(0, 255)
    else :
      r = 0
      g = 128
      b = 0
    UH.set_pixel(x, y, r, g, b)
    UH.show()
  time.sleep(1.5)
  it += 1
