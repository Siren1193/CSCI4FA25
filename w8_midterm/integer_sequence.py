#Triangular number sequence in python

def aetherflux(n):
    life = [0]
    for life_gained in range(1, n + 1):
        casts = (life_gained * (life_gained + 1)) // 2
        life.append(casts)
    return life

print(aetherflux(100))
