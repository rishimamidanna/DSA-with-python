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

def insert_at_tail(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    
    temp = head
    while temp.next != None:
        temp = temp.next
        
    temp.next = newNode  # Attach the new node at the actual tail
    return head

# --- Execution ---
head = take_input()
print("Original Linked List:")
print__LL(head)

head = insert_at_tail(head, 100)
print("Linked List after inserting 100 at the tail:")
print__LL(head)
