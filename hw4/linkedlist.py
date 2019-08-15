# Yevgeniy (Eugene) Yakovlev 
# ID: 14153285
# CS 172, Summer 2019
# Employee Payroll Homework Assignment #4

from node import Node

class LinkedList(): 

  def __init__(self):
    self.__head = None

  def getHead(self):
    return self.__head
  
  def isEmpty(self):
    return self.__head == None

  def appendNode(self, data ):
    node = Node(data)

    if self.isEmpty():
      self.__head = node
    else:
      current = self.__head
      while current.getNext() != None:
        current = current.getNext()
      current.setNext(node)

    print('\nSuccessfully added Employee!')

  def removeNode(self, id: str):
    current = self.__head
    previous = None
    found = False

    while not found:
      if current.getData().getID() == id:
        found = True
      else:
        previous = current
        current = current.getNext()

    if previous == None:
      self.__head = current.getNext()
    else:
      previous.setNext(current.getNext())

    print('\nSuccessfully removed Employee!')

  def search(self, id):
    current = self.__head
    found = False
    while current != None and not found:
      if current.getData().getID() == id:
          found = True
      else:
          current = current.getNext()

    return found, current

  def __getitem__(self, index):   # used to suppport []
    current = self.__head
    
    for i in range(index):
        current = current.getNext()

    #return current.getData() 

  def __str__(self):    # used to support print(myLinkedList)
    mystr = ''
    current = self.__head
        
    while current != None:
        mystr += str(current.getData())
        current = current.getNext()
    
    return mystr

  def __len__(self):    # used to support len(myLinkedList)
    if self.__head == None:  # if list is empty return 0
        return 0
    
    current = self.__head   #list is not empty and has at least 1 Node
    counter = 1
    
    while current.getNext() != None:
        counter += 1
        current = current.getNext()

    return counter