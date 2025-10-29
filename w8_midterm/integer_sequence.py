#Triangular number sequence in python

life = []                                               # Creates the list so we can index the amount of life gained.
def aetherflux(N):                                      # Our function to find the life gained by Aetherflux Reservoir.
    for life_gained in range(0, N + 1):                 # Loops our equation through index 0 to index N.
        casts = (life_gained * (life_gained + 1)) // 2  # Our equation for the amount of life gained from Aetherflux Reservoir
        life.append(casts)                              # Appends our result (casts) to the end of the list (life) to continue the loop.
    return life                                         # Ends our funtion, and writes our list.

print(aetherflux(100))                                  # Prints the function aetherflux to index 100.
