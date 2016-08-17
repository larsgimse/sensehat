from sense_hat import SenseHat

sense = SenseHat()

S = [0, 0, 0]  # Svart
H = [255, 255, 255]  # Hvit
R = [255, 0, 0] # Roed
Y = [255, 255,0] # Gul (Yellow)
G = [0, 255, 0] # Groenn
B = [0, 0, 255] # Blaa

# Bytt ut H (Hvit) med oensket farge for aa lage figur

pixle = [
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H,
H, H, H, H, H, H, H, H
]

sense.set_pixels(pixle)
