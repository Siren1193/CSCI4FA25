#calculator in python

def f(x,y,z): #z chooses the operator
    if (z==0):
            print("Sum = ", x+y)
    elif(z==1):
        print("Difference = ", abs(x-y))
    elif(z==2):
         print("Product =", )
    elif(z==3):
        print("Quotient =", )
    else:
         print("z =/= {0,1,2,3}")

print(f(1,2,0)) # guess sum 3
print(f(1,2,1)) # guess difference 1
print(f(1,2,5)) # z =/= {0,1,2,3}