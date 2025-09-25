#hello world in python
import array as arr
hello = "world"

print("hello", hello)

this_number = "42"

this_number = int(this_number)

print(this_number + 5)
print(this_number)
print(this_number, 5)

# Keep Notes Aswell , why write, why do, what makes sense, what confuses, etc
# Find Arrays in python docs then use them
# Find List in python docs then use them

print() # I put blank prints between sections just for clarity between what goes with what when printed in the terminal

test_array = arr.array( 
    'h', #opcode for unsigned short
    [1193, 42, 36, 36, 36,] #our list of data
)

print(type(test_array))
print(test_array) 
print(test_array.pop()) #pop returns the last thing in the list
print(test_array.count(36))

print() #linebreak

Zojja = list((3,7,6,4,5,6))
print(type(Zojja))
print(Zojja)
Zojja.sort() #this sorts the list in numeric order
print(Zojja) #this prints the list again, now in its sorted order.
print(Zojja[3]) #this prints the fourth value in the now sorted lists

New_List = list('abcdefghij1193678')
print(New_List)
New_List.sort() #I wonder how python sorts a list of numbers and characters
print(New_List)

print() #linebreak
