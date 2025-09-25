#hello world in python

hello = "world"

print("hello", hello)

this_number = "42"

this_number = int(this_number)

print(this_number + 5)
print(this_number)
print(this_number, 5)

# Keep Notes Aswell , why write, why do, what makes sense, what confuses, etc
# Find Arrays in python docs then use them
# Find List in Python docs then use them

print() # I put blank prints between secttions just for clarity between what goes with what when printed in the terminal

my_array = [7,3,8,1,3,5,2,8,4,1] #so it's basically just a binding of a group?
print(my_array[3]) #this returns the 4th value in the array since the first value is slot 0 not slot 1
print(my_array.count(1)) #there are two 1s in the array so this should return a value of 2

print() #linebreak seperator

Zojja = list((3,7,6,4,5,6)) # so a list is just an array with some extra functions 
print(type(Zojja))
print(Zojja) #this prints the list as it was written 
Zojja.sort() #this sorts the list in numeric order
print(Zojja) #this prints the list again, now in its sorted order
print(Zojja[3]) #this prints the fourth value in the sorted lists
