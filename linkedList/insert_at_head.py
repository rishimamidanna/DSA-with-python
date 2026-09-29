class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
def print_all_elements_in_linked_list(head):
  temp = head
  while(temp!=None):
    print(temp.data, end="-->")
    temp = temp.next
  print("None")
def enter_values_in_the_linkedList():
  head = None
  tail = None
  value = int(input())
  while(value!=-1):
    newNode = Node(value)
    if(head==None):
      head = newNode
      tail = newNode
    else:
      tail.next = newNode
      tail = newNode
    value = int(input())
  return head
head = enter_values_in_the_linkedList()
print_all_elements_in_linked_list(head)

def insert_at_begin(head,data):
  newNode = Node(data)
  newNode.next = head
  head = newNode
  return head

new_list = insert_at_begin(head, 99)
print_all_elements_in_linked_list(new_list)