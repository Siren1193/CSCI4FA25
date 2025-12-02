#function notation in python

import math #I imported the math module only to use math.trunc() in the last function

#f : Num -> Num
def f(x): # define the function using "def" <name>(<input list>)
        return (x + 1) # must return some value
print(f(1.5))
print(f(2), f(4), f(6), f(8), f(10), f(12), f(14), f(16))

#homework due tuesday: create 3 different functions on paper, write their types, define what they do (give them input and output arrays)
print() #linebreak

#function : 1 Num -> Num
def f(x):
        return(3 * x + 7)
print(f(1), f(2), f(3), f(4),f(5), )

print() #linebreak

#function 2 : Num1, Num2 -> Num
def f(x, b):
        return(b * pow( #pow function allows me to use exponents in my function, the syntax is pow(base, exponent)
                x - 9, 2) + 3)
print(f(9, 3), f(10, 3), f(11, 3), f(12, 3), f(13, 3), f(14, 3), )
print(f(9, 0), f(10, 1), f(11, 2), f(12, 3), f(13, 4), f(14, 5), )

print() #linebreak

#function 3  : Num -> Num
def f(x):
        b = (x + 1) #this allows me to do several terms within the operation by binding them
        b = int(b) #but since bindings themselves aren't numbers, I then need to get the result of that operation to then continue on with the rest of the operation
        return((x * b) / 2)
print(math.trunc(f(1)), math.trunc(f(2)), math.trunc(f(3)), math.trunc(f(4)), math.trunc(f(5)), math.trunc(f(6)), )

