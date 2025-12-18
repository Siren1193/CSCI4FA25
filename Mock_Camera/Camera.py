#Mock Camera in Python
import time
from PIL import Image

#image dimensions (must match the dimensions of the file imported for image_to_pixel_data.py)
width, height = 256, 256

#defines exposure stops (0-A) to 8-bit values
stops = { 
    '0': 0,
    '1': 25,
    '2': 51,
    '3': 76,
    '4': 102,
    '5': 127,
    '6': 153,
    '7': 178,
    '8': 204,
    '9': 229,
    'A': 255,
}

#simulates a mechanical shutter "OPEN" or "CLOSE"
def PHYS_SHUTTER(action: bool):
    if action == "OPEN":
        print("Shutter is now OPEN.")
    elif action == "CLOSE":
        print("Shutter is now CLOSED.")

#controls shutter timing (simulates shutter speed for exposure time)
def shutter(duration: float):
    PHYS_SHUTTER("OPEN")
    time.sleep(duration) #wait for exposure duration
    PHYS_SHUTTER("CLOSE")
    return 

#executes the shutter opening it for the amount of time written in the parenthesis
shutter(1/250)

pixel_data = [] #empty list for our next function to populate

with open("pixel_data.txt", "r") as f:
    for line in f:
        parts = line.split(" ")
        stop = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        pixel_data.append((stop, x, y)) #appends tuple to pixel_data List

img = Image.new("L", (width, height)) #creates a new image using Pillow

for stop, x, y in pixel_data:
    img.putpixel((x, y), stops[stop]) #modifies pixel (x,y) to greyscale value corresponding to stop

#saves the image
img.save("Photograph.png"); print("Photograph Saved!")