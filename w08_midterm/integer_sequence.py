#Triangular number sequence in python using Aetherflux Reservior as a reference in naming

life = []                                                                       # Creates an empty list so we can index the amount of life gained. The index of the list corresponds to the number of spells cast.
def aetherflux(N):                                                              # Names our function to find the life gained by Aetherflux Reservoir to the Nth value.
    for spells_cast in range(0, N + 1):                                         # Loops our equation through each possible number of spells cast from 0 to N.
        life_gained = (spells_cast * (spells_cast + 1)) // 2                    # Our equation for the amount of life gained from Aetherflux Reservoir.
        life.append(life_gained)                                                # Appends our result (casts) to the end of the list (life) to continue the loop until the total amount requested has been appended.
    return life                                                                 # Ends our funtion, and writes our list.

aetherflux(100)                                                                 # This fills the lists first 100 indexes so we can then call a specific one when we print our output message, though this method can be resource intensive.

print("You've gained", life[3], "life from Aetherflux Reservoir this turn!")    # Output Message, changing the value for life[N] changes the index to the specific one we choose equal to the number of spells you cast.