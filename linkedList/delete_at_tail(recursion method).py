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

def create_a_linked_list():
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

def is_tail_node(node):
    if node is None:
        return True
    if node.next is None:
        return True
    return False
def delete_at_tail_recursive(head):
  if(head is None): #base case
    return None
  if(head.next is None):
    return None
  head.next = delete_at_tail_recursive(head.next)
  return head
LL = create_a_linked_list()
__print__LL(LL)
LL = delete_at_tail_recursive(LL)
__print__LL(LL)