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
    temp.next = newNode
    return head

def insert_at_index(head, index, data):
    newNode = Node(data)
    
    # Case 1: Insert at the very beginning (index 0)
    if index == 0:
        newNode.next = head
        return newNode
    
    temp = head
    current_index = 0
    
    # Traverse to the node just before the target index
    while temp is not None and current_index < index - 1:
        temp = temp.next
        current_index += 1
        
    # Case 2: Index is out of bounds
    if temp is None:
        print(f"Error: Index {index} is out of bounds.")
        return head
        
    # Case 3: Insert in the middle or at the tail
    newNode.next = temp.next
    temp.next = newNode
    
    return head

# --- Execution ---
head = take_input()
print("\nOriginal Linked List:")
print__LL(head)

# Example 1: Insert 100 at the tail
head = insert_at_tail(head, 100)
print("After inserting 100 at the tail:")
print__LL(head)

# Example 2: Insert 99 at index 2
head = insert_at_index(head, 2, 99)
print("After inserting 99 at index 2:")
print__LL(head)