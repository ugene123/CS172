import random
from BST import *
import time
import matplotlib.pyplot as plt

def populate(n):
  if(isinstance(n, int)):
    if(n < 0):
      raise Exception('n has to be a positive integer')
    else:
      newList = []
      newBST = BST()

      for i in range(0, n):
        randInt = random.randint(0, n)
        newList.append(randInt)
        newBST.append(randInt)

      return (newList, newBST)
  else:
    raise Exception('n has to be an integer')

def findInt(list, bst):
  # Time search for Binary Search Tree
  startBST = time.time()
  # Search num in BST

  for i in range(0, len(list)):
    inBST = bst.isin(list[i])
    
  # End Search time for BST
  endBST = time.time()
  # Calculate BST time
  bstTime = endBST - startBST
  # Append to bstTime list for plotting
  bstTimes.append(bstTime)
  # Return BST time
  print('BST search time: ' + str(bstTime))

  startList = time.time()
  inList = False
  for x in range(0, len(list)):
   for y in range(0, len(list)):
     if(x == y):
       inList = True

  endList = time.time()
  listTime = endList - startList
  listTimes.append(listTime)

  print('List search time: ' + str(listTime))

  return (inList, inBST)

# def countIntInList(list, bst, num):
#   count = 0
#   for i in range(0, len(list)):
#     if i == num:
#       count += 1
  
#   return count

itemCount = []
listTimes = []
bstTimes = []

for i in range(1, 10001, 1000):
  itemCount.append(i)
  myList, myBST = populate(i)
  inList, inBST = findInt(myList, myBST)

plt.plot(itemCount, listTimes, label='List Time')
plt.plot(itemCount, bstTimes, label='BST Time')
plt.legend()
plt.show()
print()