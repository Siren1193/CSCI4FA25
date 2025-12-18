#converts an image to pixel data (stop, x, y) text file to then be used in Camera.py
from PIL import Image

#defines exposure stops (0-A) to 8-bit values for quantization
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

stop_values = list(stops.values())
#both of these lists are used as a legend for our nearest_stop function to use
stop_keys = list(stops.keys())

#finds the stop whose 8-bit value is closest
def nearest_stop(value):
    closest_index = min( #return the index of the stop whose value is closest to the pixel value
        range(len(stop_values)),
        key=lambda i: abs(stop_values[i] - value)) #choose the index whose difference is smallest
    return stop_keys[closest_index]

#converts image to pixel data and save to a text file
#each pixel will be stored as a tuple: (stop, x, y)
def image_to_pixel_data(image_path, output_file="pixel_data.txt"):
    img = Image.open(image_path).convert('L')  #converts the image imput to greyscale.
    width, height = img.size
    with open(output_file, "w") as f: #loops through every pixel in the image (left -> right, top -> bottom)
        for y in range(height):
            for x in range(width):
                pixel_value = img.getpixel((x, y)) #get pixel value
                stop = nearest_stop(pixel_value) #quantize pixel value
                f.write(f"({stop}, {x}, {y})\n") #write to file

    print(f"Pixel data saved to {output_file}.")

#imported image has to match width, height in Camera.py otherwise it will create error.
image_to_pixel_data("Orchid_256.png")
