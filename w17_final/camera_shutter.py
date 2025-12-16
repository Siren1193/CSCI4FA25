import time

def PHYS_SHUTTER(action):
    if action == "OPEN":
        print("Shutter is now OPEN.")
    elif action == "CLOSE":
        print("Shutter is now CLOSED.")
    else:
        print("Unknown shutter action!")

def shutter(duration: float):
    PHYS_SHUTTER("OPEN")
    time.sleep(duration) #this creates a gap of time between the shutter opening and the shutter closing.
    PHYS_SHUTTER("CLOSE")
    return 

shutter(1/250)

