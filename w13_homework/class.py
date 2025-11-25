#conditional choice

def f(x,y,z): #z chooses the operator
    if (z==0):
            print("sum", x+y)
    elif(z==1):
        print("difference , abs(x-y)")
    else:
         print("z =/= {0,1,2}")

print(f(1,2,0)) # guess sum 3

print(f(1,2,1)) # guess difference 1

print(f(1,2,5)) # z =/= {0,1}