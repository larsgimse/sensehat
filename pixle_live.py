from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

s = [0, 0, 0]  # Svart
h = [255, 255, 255]  # Hvit
r = [255, 0, 0] # Roed
y = [255, 255,0] # Gul (Yellow)
g = [0, 255, 0] # Groenn
b = [0, 0, 255] # Blaa

# Bytt ut H (Hvit) med oensket farge for aa lage figur

pixle1 = [
h,h,h,h,h,h,h,h,
h,r,r,h,h,r,r,h,
h,r,g,h,h,r,g,h,
h,h,h,h,h,h,h,h,
h,h,h,r,r,h,h,h,
h,r,h,h,h,h,r,h,
h,h,r,r,r,r,h,h,
h,h,h,h,h,h,h,h
  ]
  
pixle2 = [
h,h,h,h,h,h,h,h,
h,r,r,h,h,r,r,h,
h,g,r,h,h,g,r,h,
h,h,h,h,h,h,h,h,
h,h,h,r,r,h,h,h,
h,h,h,h,h,h,h,h,
h,r,r,r,r,r,r,h,
h,h,h,h,h,h,h,h
  ]

while True: #loekke for aa bytte mellom pixle1 og pixle2
  sense.set_pixels(pixle1)
  sleep(1)
  sense.set_pixels(pixle2)
  sleep(1)
