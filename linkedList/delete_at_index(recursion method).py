class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def __print__LL(head):
    temp = head
    while temp is not None:
        print(temp.value, end="->")
        temp = temp.next
    print("None")
    return head

def take_input():
    head = None
    tail = None
    value = int(input("Enter node value (-1 to stop): "))
    while value != -1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter node value (-1 to stop): "))
    return head

def delete_at_index_using_recursion(head, index):
    # Base Case 1: If we reach the end and didn't find the index
    if head is None:
        print("Index is out of bounds")
        return None
    
    # Base Case 2: If we reached the target index, skip this node
    if index == 0:
        return head.next
    
    # Recursive step: move to the next node and decrease the index
    head.next = delete_at_index_using_recursion(head.next, index - 1)
    
    return head

# --- Execution ---
head = take_input()

print("\nOriginal Linked List:")
__print__LL(head)

# Test deleting node at index 2 using recursion
head = delete_at_index_using_recursion(head, 2)

print("After recursive deletion at index 2:")
__print__LL(head)