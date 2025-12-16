#Mock Camera in Python
import time #for shutter timing
from PIL import Image #allows us to create images in python

#image dimensions for PIL
#in theory this could be expanded to whatever size needed, image imported for use in image_to_pixel_data.py has to match in width and height to this string
width, height = 256, 256 

#defines dynamic range stops 0-9, A, B
#this maps discrete stops to 8-bit greyscale values (0=black, 255=white)
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

#function to simulate mechanical shutter
#parameters: action(str): either "OPEN" or "CLOSE"
def PHYS_SHUTTER(action):
    if action == "OPEN":
        print("Shutter is now OPEN.")
    elif action == "CLOSE":
        print("Shutter is now CLOSED.")
    else:
        print("Unknown shutter action!")

#function to control shutter timing
def shutter(duration: float):
    PHYS_SHUTTER("OPEN")
    time.sleep(duration) #this creates a gap of time between the shutter opening and the shutter closing simulating exposure time.
    PHYS_SHUTTER("CLOSE")
    return 

#executes the shutter opening it for the amount of time written in the parenthesis
shutter(1/250)

#defines pixel data (stop, x, y)
pixel_data = [] #empty list for our next function to populate

with open("pixel_data.txt", "r") as f:
    for line in f:
        line = line.replace("(", "").replace(")", "") #removes any extra parantheses and whitespace
        parts = line.split(",")
        stop = parts[0].strip()   #stop value as string
        x = int(parts[1].strip()) # converts x coordinate to int
        y = int(parts[2].strip()) # converts y coordinate to int
        pixel_data.append((stop, x, y)) #appends tuple to pixel_data List

#creates a new image in Pillow using L mode (8-bit greyscale)
img = Image.new("L", (width, height))

#loop over pixel_data to place pixel in the image
for stop, x, y in pixel_data:
    img.putpixel((x, y), stops[stop]) # set pixel (x,y) to greyscale value corresponding to stop

#saves the image file
img.save("Photograph.png")