from sense_hat import SenseHat

sense = SenseHat()

S = [0, 0, 0]  # Svart
H = [255, 255, 255]  # Hvit
R = [255, 0, 0] # Rød
Y = [255, 255,0] # Gul (Yellow)
G = [0, 255, 0] # Grønn
B = [0, 0, 255] # Blå

# Bytt ut H (Hvit) med ønsket farge for å lage figur

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
