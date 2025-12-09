#calculator in python

def f(x,y,z):
    if (z==0):
            print("Sum = ", x+y)
    elif(z==1):
        print("Difference = ", x-y)
    elif(z==2):
         print("Product =", x*y )
    elif(z==3):
        print("Quotient =", x/y )
    else:
         print("z =/= {0,1,2,3}")

#to use this function print(f(x,y,z))
#x defines the left number
#y defines the right number
#z chooses the operator
    #z=0 addition
    #z=1 subtraction
    #z=2 multiplication
    #x=3 division 
print(f(5,5,0)) # Sum = 10
print(f(1,-1,0)) # Sum = 0
print(f(0,-1,1)) # Difference = 1
print(f(0,5,3)) # Quotent = 0
print(f(4,2,3)) # Quotent = 2
print(f(2,1,2)) # Product = 2
print(f(3,2,2)) # Product = 6