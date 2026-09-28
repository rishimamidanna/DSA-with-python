class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Move these out of the class (no indentation)
def print__LL(head):
    temp = head 
    while (temp != None):
        print(temp.value,end="->")
        temp = temp.next 
    print("None")
    return 

def take_input():
    head = None
    tail = None
    value = int(input("Enter node value (-1 to stop): "))
    while (value != -1):
        newNode = Node(value)
        if (head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter node value (-1 to stop): "))
    return head

# Execution
newhead = take_input()
print__LL(newhead)