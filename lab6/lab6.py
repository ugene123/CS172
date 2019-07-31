from stack import Stack

def postfix(exp):
  # Split expression by space
  parts = exp.split(' ')
  # Create empty stack
  stack = Stack()
  # Loop through each char in list
  for part in parts:
    # When operator is seen
    if(part in ['+', '-', '*', '/']):
      # Pop top 2 items on stack
      itemOne = int(stack.pop())
      itemTwo = int(stack.pop())
      
      result = 0
      if(part == '+'):
        result = itemTwo + itemOne
      elif(part == '-'):
        result = itemTwo - itemOne
      elif(part == '*'):
        result = itemTwo * itemOne
      elif(part == '/'):
        result = itemTwo / itemOne

      stack.push(float(result))

    else: 
      # Push Numbers onto Stack as read from input
      if(isinstance(int(part), int)):
        stack.push(part)

  return stack.top()

print('Welcome to the Postfix Calculator')

continuePostfix = True
while (continuePostfix):
  userInput = input("Enter the postfix expression: \n")

  if(userInput == 'exit'):
    continuePostfix = False
  else:   
    try:
      answer = postfix(userInput)
      print('Result: ' + str(answer))
    except:
      print('Please enter a valid post fix expression!')

