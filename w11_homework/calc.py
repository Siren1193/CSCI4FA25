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
f(5,5,0) # Sum = 10
f(1,-1,0) # Sum = 0
f(0,-1,1) # Difference = 1
f(0,5,3) # Quotent = 0
f(4,2,3) # Quotent = 2
f(2,1,2) # Product = 2
f(3,2,2) # Product = 6

