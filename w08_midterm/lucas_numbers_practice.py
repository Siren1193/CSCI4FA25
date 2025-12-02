#lucas numbers in python, practice example for midterm
def lucas(named):
    delta = [2,1] #delta is the name of the list
    #0 → 2
    #1 → 1
    #>1 → (n-1)+(n-2)
    for n in range(2,named):
        #for [number] which is equal to 2, 3, 4, 5
        delta.append(delta[n - 1] + delta[n - 2]) #adds the output of the function to the next index in the list
    return delta

print("Lucas numbers are:", lucas(10))