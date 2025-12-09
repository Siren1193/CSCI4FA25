#stack (first in, last out)

stack = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
head = 0 #the head of the queue is always the 0th index in the list

def tail(stack):
    return len(stack) - 1

def push(stack,e):
    stack.append(e)
    return stack

def pop(stack):
    return stack.pop(tail(stack))

print(stack)
print(pop(stack))
print(stack)
print(push(stack,5))
