from sense_hat import SenseHat

sense = SenseHat()

s = [0, 0, 0]  # Svart
h = [255, 255, 255]  # Hvit
r = [255, 0, 0] # Roed
y = [255, 255,0] # Gul (Yellow)
g = [0, 255, 0] # Groenn
b = [0, 0, 255] # Blaa

# Bytt ut h (Hvit) med oensket farge for aa lage figur

pixle = [
h,h,r,r,r,r,h,h,
h,r,h,h,h,h,r,h,
r,h,r,h,r,h,h,r,
r,h,r,h,r,h,h,r,
r,h,h,h,h,r,h,r,
r,h,r,r,r,h,h,r,
h,r,h,h,h,h,r,h,
h,h,r,r,r,r,h,h
]

sense.set_pixels(pixle)
