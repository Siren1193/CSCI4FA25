#Triangular number sequence in python
#x(x-1)/2
def aetherflux(y):
    life = [0]
    for casts in range(1,y):
        life.append(life[(casts * (casts + 1) // 2)])
    return life

print(aetherflux(10))