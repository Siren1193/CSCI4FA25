from PIL import Image

#image size
width, height = 256, 256

#define dynamic range stops 0-9, A, B
stops = {
    '0': 0,
    '1': 23,
    '2': 46,
    '3': 69,
    '4': 92,
    '5': 115,
    '6': 138,
    '7': 161,
    '8': 184,
    '9': 207,
    'A': 230,
    'B': 255,
}

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
#displays the image file
img.show()