#queue (waiting in line)

q = [] #creates an empty list
head = 0 #the head of the queue is always the 0th index in the list

def tail(q): 
    return len(q) #how ever many elements in q, thats where the tail is

def push(q,e): #e matches whatever is in q. push puts element e into the queue q
    q.append(e) # q = [.......,e]
    return q

def pop(q): #pop
    return q.pop(head) 


