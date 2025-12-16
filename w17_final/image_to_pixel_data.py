from PIL import Image

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

stop_values = list(stops.values())
stop_keys = list(stops.keys())

def nearest_stop(value):
    """Return the key of the stop closest to the given pixel value."""
    closest_index = min(range(len(stop_values)), key=lambda i: abs(stop_values[i] - value))
    return stop_keys[closest_index]

def image_to_pixel_data(image_path, output_file="pixel_data.txt"):
    """Convert image to pixel data and save to a text file."""
    img = Image.open(image_path).convert('L')  # L = grayscale
    width, height = img.size

    with open(output_file, "w") as f:
        for y in range(height):
            for x in range(width):
                pixel_value = img.getpixel((x, y))
                stop = nearest_stop(pixel_value)
                f.write(f"({stop}, {x}, {y})\n")

    print(f"Pixel data saved to {output_file}.")

#imported image has to be 256x256
image_to_pixel_data("Orchid_256.png")
