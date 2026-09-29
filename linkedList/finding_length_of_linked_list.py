class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print__LL(head):
    temp = head 
    while (temp != None):
        print(temp.value, end="->")
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

# Your recursive function
def find_length_of_linkedList(head):
    if(head == None):
        return 0
    recursionAnswer = find_length_of_linkedList(head.next)
    return 1 + recursionAnswer

# --- Execution (Call and Print) ---
headofLL = take_input()
print("Linked List:")
print__LL(headofLL)

length = find_length_of_linkedList(headofLL)
print("Length of Linked List (Recursive):", length)